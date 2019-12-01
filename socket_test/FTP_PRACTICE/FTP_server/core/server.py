#!/usr/bin/python3.5

import socketserver,json,configparser,os,hashlib,shutil
from conf import settings
from core import mylogger

STATUS_CODE  = {
    250 : "Invalid cmd format, e.g: {'action':'get','filename':'test.py','size':344}",
    251 : "Invalid cmd ",
    252 : "Invalid auth data",
    253 : "Wrong username or password",
    254 : "Passed authentication",
    255 : "Filename doesn't provided",
    256 : "File doesn't exist on server",
    257 : "ready to send file",
    258 : "md5 verification",

    800 : "This file exist,but hasn't transfered completely,do you want to continue? ",
    801 : "This file exist !",
    802 : "ready to receive datas",
    803 : "This is the root directory",

    900 : "md5 valdate successfully",
    901 : "md5 valdate failed"
}

my_log = mylogger.MyLogger()

class MyServerHandler(socketserver.BaseRequestHandler):

    def handle(self):
        '''
        每一个tcp连接建立后，都会调用该类生成的一个对象，并执行此函数中定义的逻辑，
        该函数是调用所有ftp功能的入口，功能均通过其分发到此类中的其他方法
        :return:
        '''
        while True:
            data = self.request.recv(1024).strip()
            if len(data) == 0:break
            data = json.loads(data.decode('utf-8'))
            '''
            可接收的客户端请求数据格式：
            {'action':'auth','username':'zx','password':'123'}
            '''
            if data.get('action'):
                if hasattr(self,'_%s'%data.get('action')):
                    func = getattr(self,'_%s'%data.get('action'))
                    func(**data)
                else:
                    # print("Invalid CMD.") #后期修改为记录日志到日志文件
                    my_log.logger.error("Invalid CMD.")
                    self.send_response(251)
            else:
                # print("Invalid CMD Format.") #后期修改为记录日志到日志文件
                my_log.logger.error("Invalid CMD Format.")
                self.send_response(250)


    def send_response(self,scode,data=None):
        '''
        发送数据至客户端
        :param scode:
        :param data:
        :return:
        '''
        response = {'status_code':scode,'status_msg':STATUS_CODE[scode]}
        if data:
            response.update(data)
        self.request.sendall(json.dumps(response).encode('utf-8'))


    def _auth(self,**data):
        '''
        认证传递过来的用户名密码是否存在，如果存在，是否正确
        :param data:
        :return:
        '''
        if not data.get('username') or not data.get('password'):
            self.request.sendall(252)
            return

        user = self.authenticate(data.get('username'),data.get('password'))
        if not user:
            # print("Wrong username or password") #后期修改为记录日志到日志文件
            my_log.logger.critical("Wrong username or password")
            self.send_response(253)
        else:
            # print("%s Passed authentication"%user) #后期修改为记录日志到日志文件
            my_log.logger.info("%s Passed authentication"%user)
            self.user = user
            self.send_response(254)
            self.mainPath = os.path.join(settings.BASE_DIR,'home',self.user)


    def authenticate(self,username,password):
        '''
        比较客户端发过来的用户信息是否和服务器配置文件中保存的信息一致，
        验证成功返回用户名，否则返回None
        :param username:
        :param password:
        :return:
        '''
        cfp = configparser.ConfigParser()
        cfp.read(settings.ACC_PATH)
        if username in cfp.sections():
            pwd = cfp[username]['password']
            if pwd == password:
                return username


    def _post(self,**data):
        '''
        可接收的客户端请求数据格式：
        {'action':'post','file_name':'test','file_size':12345,'target_path':'images'}
        '''
        file_name = data.get('file_name')
        file_size = data.get('file_size')
        target_path = data.get('target_path')
        file_abs_path = os.path.join(self.mainPath,target_path,file_name)

        has_recvd = 0
        if os.path.exists(file_abs_path): #如果要上传的文件已经存在
            serv_file_size = os.path.getsize(file_abs_path)
            if serv_file_size < file_size: #如果要上传的文件比服务器上的文件小
                self.request.sendall(b'800')
                does_cont = self.request.recv(1024).decode('utf-8').lower()
                if does_cont == "y" or does_cont == "yes": #如果想要进行断点续传
                    self.request.sendall(str(serv_file_size).encode('utf-8'))
                    has_recvd = serv_file_size
                    f = open(file_abs_path,'ab')
                else:
                    #如果想要覆盖原文件
                    f = open(file_abs_path,'wb')
            else:
                self.request.sendall(b'801') #如果文件存在并且和要上传的文件一样大
                return
        else:
            self.request.sendall(b'802')
            f = open(file_abs_path,'wb')

        md5_obj = hashlib.md5()

        res_data = b''
        while has_recvd < file_size:
            res_data = self.request.recv(1024)
            md5_obj.update(res_data)
            has_recvd += len(res_data)
            f.write(res_data)

        f.close()

        recv_md5_val = md5_obj.hexdigest()
        self.request.sendall(b"ok")  # 解决粘包
        send_file_val = self.request.recv(1024).decode("utf8")
        self.request.sendall(recv_md5_val.encode('utf-8'))

        cli_md5_result = self.request.recv(1024).decode('utf-8') # 接收客户端发来的md5验证结果
        print(STATUS_CODE[int(cli_md5_result)])
        if send_file_val == recv_md5_val:
            print("send_file_val", send_file_val)
            self.request.sendall("900".encode("utf8"))
        else:
            self.request.sendall("901".encode("utf8"))


    # def _post_md5(self, **data):
    #     '''
    #     附加了计算上传的文件的md5码功能的上传
    #     {'action':'post_md5','file_name':'test','file_size':12345,'target_path':'zx/images'}
    #     :param data:
    #     :return:
    #     '''
    #     file_name = data.get("file_name")
    #     file_size = data.get("file_size")
    #     target_path = data.get("target_path")
    #     abs_path = os.path.join(self.mainPath, target_path, file_name)
    #
    #     has_received = 0
    #     if os.path.exists(abs_path):
    #         has_file_size = os.stat(abs_path).st_size
    #         if has_file_size < file_size:
    #             self.request.sendall(b"800")
    #             is_continue = str(self.request.recv(1024), "utf8")
    #             if is_continue == "Y":
    #                 self.request.sendall(bytes(str(has_file_size), "utf8"))
    #                 has_received += has_file_size
    #                 f = open(abs_path, "ab")
    #             else:
    #                 f = open(abs_path, "wb")
    #         else:
    #             self.request.sendall(b"801")
    #             return
    #     else:
    #         self.request.sendall(b"802")
    #         f = open(abs_path, "wb")
    #
    #     if data.get('md5'): #如果需要计算文件的md5码
    #         md5_obj = hashlib.md5()
    #         recv_file_md5 = ''
    #         while has_received < file_size:
    #             try:
    #                 data = self.request.recv(1024)
    #                 if not data:
    #                     raise Exception
    #             except Exception:
    #                 break
    #
    #             f.write(data)
    #             has_received += len(data)
    #             recv_file_md5 = md5_obj.update(data) #根据收到的文件不断更新md5码
    #         else: #接收完所有的文件数据后，接收md5码
    #             self.request.sendall(b"ok")  # 解决粘包
    #             send_file_md5 = self.request.recv(1024).decode("utf8")
    #             if send_file_md5 == recv_file_md5:
    #                 print("send_file_md5", send_file_md5)
    #                 self.request.sendall("900".encode("utf8"))
    #             else:
    #                 self.request.sendall("901".encode("utf8"))
    #     else: # 如果不需要进行md5校验
    #         while has_received < file_size:
    #             try:
    #                 data = self.request.recv(1024)
    #                 if not data:
    #                     raise Exception
    #             except Exception:
    #                 break
    #         f.write(data)
    #         has_received += len(data)
    #
    #     f.close()


    def _get(self, **data):
        '''
        具有md5校验功能的文件下载实现；
        首先判断客户端是不是有同名文件，如果有，大小不是0，并且客户端选择续传，就需要将服务器端
        指针移动到客户端发来的文件大小处，再发送文件，否则从头发送文件
        {'action':'get','file_name':'images/test.jpg','cli_file_size':1234,'file_continue':'y'}
        :param data:
        :return:
        '''
        file_continue = data.get('file_continue')
        cli_file_size = data.get('cli_file_size')
        file_name = data.get('file_name')
        abs_path = os.path.join(self.mainPath,file_name)

        has_send = 0
        if os.path.isfile(abs_path):
            # 如果想下载的文件存在于服务器上
            if cli_file_size > 0 and file_continue.lower() == 'y':
                # 需要进行断点续传
                f = open(abs_path,'rb')
                has_send = cli_file_size
            # 客户端需要从头接收数据
        else:
            # 如果想下载的文件不存在
            my_log.logger.warning("File %s doesn't exist on server"%file_name)
            self.request.sendall("File doesn't exist on server".encode('utf-8'))
            return

        file_size = os.path.getsize(abs_path)
        self.request.sendall(str(file_size-has_send).encode('utf-8')) # 发送要下载的文件大小给客户端
        self.request.recv(1024) # 接收客户端发来的确认，防止粘包

        md5_obj = hashlib.md5()

        f = open(abs_path, 'rb')
        f.seek(has_send)
        while has_send < file_size:
            line = f.read(1024)
            self.request.sendall(line)
            has_send += len(line)
            md5_obj.update(line)
        f.close()

        recv_file_val = self.request.recv(1024).decode('utf-8')  # 客户端接收完数据后需要发送自己的md5校验码过来，解决粘包

        send_file_val = md5_obj.hexdigest()
        self.request.sendall(send_file_val).decode("utf8") #发送md5码给客户端

        if recv_file_val == send_file_val:
            # print('%s has sended completely!'%abs_path) #需要记录到日志文件中
            my_log.logger.info('%s has sended completely!'%abs_path)
        else:
            # print('unkown error happened when client was downloading %s'%abs_path)
            my_log.logger.critical('unkown error happened when client was downloading %s'%abs_path)


    def _ls(self,**data):
        '''
        可以显示该用户下的任意目录中的内容
        {'action':'ls','dirname':'images'}
        :param data:
        :return:
        '''
        abs_dirname = os.path.join(self.mainPath,data.get('dirname'))

        if os.path.isdir(abs_dirname):
            file_list = os.listdir(abs_dirname)
            if not file_list:
                file_str = "<empty directory>"
            else:
                file_str = '\n'.join(file_list)
        elif os.path.isfile(abs_dirname):
            file_str = "<not a directory>"
        else:
            file_str = "<required directory does not exist>"

        my_log.logger.info(file_str)
        self.request.sendall(file_str.encode('utf-8'))


    def _cd(self,**data):
        '''
        可接收的客户端请求数据格式：
        {'action':'cd','path':'images'}
        '''
        path = data.get('path')
        if path == '..':
            if self.mainPath == os.path.join(settings.BASE_DIR,'home',self.user):
                pass
            else:
                self.mainPath = os.path.dirname(self.mainPath)
        else:
            self.mainPath = os.path.join(self.mainPath,path)

        self.request.sendall(self.mainPath.encode('utf-8'))


    def _mkdir(self, **data):
        '''
        可接收的客户端请求数据格式：
        {'action':'mkdir','dirname':'docs'}
        '''
        dirname = data.get("dirname")
        tar_path = os.path.join(self.mainPath, dirname)
        if not os.path.exists(tar_path):
            os.makedirs(tar_path)
            my_log.logger.info("mkdir %s success!"%tar_path)
            self.request.send(b"mkdir_success!")
        else:
            my_log.logger.warning("directory %s exists!"%tar_path)
            self.request.send(b"dir_exists!")


    def _rm(self, **data):
        '''
        可接收的客户端请求数据格式：
        {'action':'rm','dirname':'docs'}
        '''
        dirname = data.get("dirname")
        tar_path = os.path.join(self.mainPath, dirname)

        if os.path.exists(tar_path): # 如果要删除的目录或者文件存在
            if os.path.isfile(tar_path):
                os.remove(tar_path)  # 删除文件
            else:
                shutil.rmtree(tar_path)  # 删除目录

            my_log.logger.info("rm_success!")
            self.request.sendall(b"rm_success!")
        else:
            # 如果要删除的目录或者文件不存在，直接报错
            my_log.logger.warning("the file or dir does not exist!")
            self.request.sendall(b"the file or dir does not exist!")


    def _pwd(self, **data): #显示用户当前所在目录
        '''
        可接收的客户端请求数据格式：
        {'action':'pwd'}
        '''
        self.request.sendall(self.mainPath.replace(settings.BASE_DIR,'').encode('utf-8'))
        # 不显示系统全路径，只显示home开始的相对路径