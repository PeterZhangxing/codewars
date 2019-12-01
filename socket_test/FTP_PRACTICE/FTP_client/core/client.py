#!/usr/bin/python3.5

import json,os,sys,time,hashlib,socket,optparse,re

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

class FTPClient(object):

    def __init__(self):
        '''
        实例化客户端对象时，获取附加在脚本后的各个参数的值，保存在字典和列表中
        '''
        self.op = optparse.OptionParser()
        self.op.add_option("-s","--server",dest="server")
        self.op.add_option("-P","--port",dest="port")
        self.op.add_option("-u","--username",dest="username")
        self.op.add_option("-p","--password",dest="password")
        self.options,self.args = self.op.parse_args()
        # option中保存的是自己定义的选项的字典，其余未定义的值保存在args定义的列表中
        self.main_path = os.path.dirname(os.path.abspath(__file__))

        self.verify_ops() # 校验输入的ip地址和端口是不是符合规范
        self.create_connection() # 和FTP服务器建立连接

        self.last = 0


    def verify_ops(self):
        '''
        校验输入的ip地址和端口是不是符合规范
        :return:
        '''
        ip_exp = re.compile(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
        if self.options.server and self.options.port:
            if int(self.options.port) > 1024 and int(self.options.port) < 65534:
                if ip_exp.match(self.options.server):
                    return
                else:
                    exit("wrong ipv4 format")
            else:
                exit("wrong port format")
        else:
            exit("server ip and port cannot be empty")


    def create_connection(self):
        '''
        和FTP服务器建立连接
        :return:
        '''
        self.sock = socket.socket()
        self.sock.connect((self.options.server,int(self.options.port)))


    def authenticate(self):
        '''
        校验用户名密码是否正确
        :return:
        '''
        if self.options.username and self.options.password:
            return self.auth_res(self.options.username,self.options.password)
        else:
            username = input('enter your username: ')
            password = input('enter your password: ')
            return self.auth_res(username,password)


    def auth_res(self,username,password):
        '''
        发送本地的用户名密码给服务器端，并比将服务器返回的结果返回给认证函数authenticate
        :param username:
        :param password:
        :return:
        '''
        info = {
            'action':'auth',
            'username':username,
            'password':password
        }
        self.sock.sendall(json.dumps(info).encode('utf-8'))
        res = json.loads(self.sock.recv(1024).decode('utf-8'))
        if res.get('status_code') == 254: # 如果通过认证
            self.user = username
            self.current_path = '/' + username
            return True
        else:
            print(res.get("status_msg"))
            return False


    def inter_active(self):
        '''
        所有交互命令的总入口，认证通过后就进入接收命令交互的循环
        :return:
        '''
        if self.authenticate():
            print('authenticated start communicating: ')

            while True:
                cmd = input("[%s]"%self.current_path).strip()
                if len(cmd) == 0:continue
                if cmd == 'quit' or 'exit':
                    exit('you have quited this programme')

                cmd_li = cmd.split()
                if hasattr(cmd_li[0]):
                    func = getattr(self,"_%s"%cmd_li[0])
                    func(cmd_li)
                else:
                    print('cmd dose not exist')


    def dis_ppercent(transed_data_size, total_data_size):
        '''
        显示文件传输进度的功能模块
        :param transed_data_size:
        :param total_data_size:
        :return:
        '''
        percentage = int(float(transed_data_size) / float(total_data_size) * 100)
        sys.stdout.write("%s%% %s\r" % (percentage, '#' * percentage))
        sys.stdout.flush()


    def _post(self,cmd_li):
        '''
        上传本地文件服务器端的功能模块
        :param cmd_li:
        :return:
        '''
        action,local_path,target_path = cmd_li

        local_path = os.path.join(self.main_path,local_path)
        file_name = os.path.basename(local_path)
        file_size = os.path.getsize(local_path)

        head = {
            'action':'post',
            'file_name':file_name,
            'file_size':file_size,
            'target_path':target_path
        }

        self.sock.sendall(json.dumps(head).encode('utf-8'))
        # 把需要上传的文件的信息发送给服务器端

        recv_code = int(self.sock.recv(1024).decode('utf8'))
        # 获取服务器返回的状态码，根据状态码进行后续操作

        has_send = 0
        if recv_code == 800:
            cli_choice = input("file already exists,do you want to continue: (y/n)").strip()
            if cli_choice.lower() == 'y':
                self.sock.sendall('y'.encode('utf-8'))
                start_pos = int(self.sock.recv(1024).decode('utf-8'))
                has_send = start_pos
            else:
                self.sock.sendall('n'.encode('utf-8'))
        elif recv_code == 801:
            print(STATUS_CODE[801])
            return

        f = open(local_path,'rb')
        f.seek(has_send)
        md5_obj = hashlib.md5()

        start = time.time()
        while has_send < file_size:
            tmp_data = f.read(1024)
            self.sock.sendall(tmp_data)
            has_send += len(tmp_data)
            md5_obj.update(tmp_data)
            self.dis_ppercent(has_send,file_size) # 显示文件上传进度

        f.close()
        end = time.time()
        print('uploading %s costs %s s'%(file_name,(end-start)))

        cli_md5_val = md5_obj.hexdigest()
        if self.sock.recv(1024).decode('utf-8').upper() == 'OK':
            self.sock.sendall(cli_md5_val.encode('utf-8'))
            server_md5_val = self.sock.recv(1024).decode('utf-8')

            if server_md5_val == cli_md5_val:
                print('uploading %s successfully'%file_name)
                self.sock.sendall('900'.encode('utf-8'))
            else:
                print('md5_code does not match')
                self.sock.sendall('901'.encode('utf-8'))

            server_md5_result = self.sock.recv(1024).decode('utf-8') # 接收server端发送来的验证结果
            print(STATUS_CODE[int(server_md5_result)])

        else:
            print('unkown mistakes happened during uploading')


    def _get(self,cmd_li):
        '''
        从服务器端下载文件的功能模块
        {'action':'get','file_name':'images/test.jpg','cli_file_size':1234,'file_continue':'y'}
        :param cmd_li:
        :return:
        '''
        # 通过命令获取构建数据头的参数
        action, file_name = cmd_li

        # 生成想要下载的文件在本地的绝对路径，用于后续判断该文件在本地是否已经存在
        local_path = os.path.join(self.main_path, os.path.basename(file_name))

        cli_file_size = 0
        file_continue = "n"

        if os.path.isfile(local_path):
            cli_file_size = os.path.getsize(local_path)
            file_continue = input('File exists do you want to continue?(y/n)').strip().lower()
            while file_continue != 'y' or file_continue != 'n':
                print('invalid input,you can only input y or n')
                file_continue = input('File exists do you want to continue?(y/n)').strip().lower()

        head = {
            'action': 'get',
            'file_name': file_name,
            'cli_file_size': cli_file_size,
            'file_continue':file_continue
        }

        self.sock.sendall(json.dumps(head).encode('utf-8'))
        # 把需要上传的文件的信息发送给服务器端

        recv_code = self.sock.recv(1024).decode('utf8')
        # 获取服务器返回的信息，根据信息进行后续操作

        if recv_code == STATUS_CODE[256]:
            print(STATUS_CODE[256])
            return
        else:
            ser_file_size = int(recv_code)

        if cli_file_size > 0 and file_continue == 'y':
            f = open(local_path,'ab')
        else:
            f = open(local_path,'wb')

        md5_obj = hashlib.md5()
        start_time = time.time()
        while cli_file_size < ser_file_size:
            tmp_data = self.sock.recv(1024)
            md5_obj.update(tmp_data)
            f.write(tmp_data)
            cli_file_size += len(tmp_data)
            self.dis_ppercent(cli_file_size,ser_file_size)
        f.close()

        end_time = time.time()
        print(print('downloading %s costs %s s'%(file_name,(end_time-start_time))))

        get_file_val = md5_obj.hexdigest()
        self.sock.sendall(get_file_val.encode('utf-8')) # 发送客户端的校验码给服务器端

        put_file_val = self.sock.recv(1024).decode('utf-8') # 接收客户端发来的校验码

        if put_file_val == get_file_val:
            print('%s has downloaded completely and correctly!'%file_name) #需要记录到日志文件中
        else:
            print('unkown error happened when client was downloading %s'%file_name)


    def _cd(self,cmd_li):
        '''
        进入子目录或
        :param cmd_li:
        :return:
        '''
        head = {
            'action':'cd',
            'path':cmd_li[1]
        }
        self.sock.sendall(json.dumps(head).encode('utf8'))
        self.current_path = "/" + os.path.basename(self.sock.recv(1024).decode('utf8'))


    def __ls(self,cmd_li):
        '''
        仅能显示当前目录下文件的ls,改造成可以显示自己名字下的所有文件夹内的内容
        :param cmd_li:
        :return:
        '''
        head = {
            'action':'ls',
            'dirname':cmd_li[1]
        }
        self.sock.sendall(json.dumps(head).encode('utf8'))
        file_li = self.sock.recv(1024).decode('utf8')
        print(file_li)


    def _mkdir(self,cmd_li):
        '''
        在服务器上创建目录
        :param cmd_li:
        :return:
        '''
        head = {
            'action':'mkdir',
            'dirname':cmd_li[1]
        }
        self.sock.sendall(json.dumps(head).encode('utf8'))
        mk_res = self.sock.recv(1024).decode('utf8')
        print(mk_res)


    def _rm(self,cmd_li):
        '''
        从服务器上删除目录或文件
        :param cmd_li:
        :return:
        '''
        head = {
            'action':'rm',
            'dirname':cmd_li[1]
        }
        self.sock.sendall(json.dumps(head).encode('utf8'))
        rm_res = self.sock.recv(1024).decode('utf8')
        print(rm_res)


    def _pwd(self,cmd_li):
        '''
        显示当前在服务器的哪个文件路径下
        :param cmd_li:
        :return:
        '''
        head = {
            'action':'pwd',
        }
        self.sock.sendall(json.dumps(head).encode('utf8'))
        pwd_res = self.sock.recv(1024).decode('utf8')
        print(pwd_res)
