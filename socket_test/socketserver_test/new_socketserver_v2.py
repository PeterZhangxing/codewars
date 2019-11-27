#!/usr/bin/python3.5

import socketserver,subprocess,struct,json,os

user_info = {'zx':'123','honda':'abcd','toyota':'redhat'}

class MySS(socketserver.BaseRequestHandler):

    def my_send(self,msg):
        '''
        通过该对象建立的TCP连接发送数据的函数
        :param msg:
        :return:
        '''
        length = len(msg)
        data_len = struct.pack('i', length)
        self.request.send(data_len)
        if type(msg) is str:
            self.request.send(msg.encode('utf-8'))
        else:
            self.request.send(msg)


    def my_recv(self, buffer):
        '''
        收取通过TCP连接发送过来的数据，不会黏包
        :param buffer:
        :return: 从客户端接收到的比特格式的内容
        '''
        res_dsize = self.request.recv(4)
        res_dsize = struct.unpack('i', res_dsize)[0]

        rev_dsize = 0
        res_data = b''
        while rev_dsize < res_dsize:
            res_data += self.request.recv(buffer)
            rev_dsize = len(res_data)

        return res_data #返回从客户端接收到的比特格式的内容


    def auth_user(self,buffer):
        '''
        认证登录socket_server的用户的信息
        :param buffer:
        :return: 是否是有效用户
        '''
        recv_uinfo = self.my_recv(buffer).decode('utf-8')
        uinfo = json.loads(recv_uinfo) #{'name':'zx','passwd':'123'}

        if uinfo['name'] in user_info.keys():
            if uinfo['passwd'] == user_info[uinfo['name']]:
                print('Authorised user %s login!'%(uinfo['name']))
                return True
            else:
                print("password is not correct")
                return False
        else:
            print('user dose not exist')
            return False


    def excmd(self,buffer,cmd):
        '''
        完成远程执行命令的函数
        :param buffer:
        :param cmd:
        :return: 发送命令执行的结果给客户端
        '''
        try:
            if not cmd:
                self.my_send('The value of cmd cannot be null!')
            else:
                res = subprocess.Popen(cmd, shell=True,
                                       stderr=subprocess.PIPE,
                                       stdout=subprocess.PIPE,
                                       stdin=subprocess.PIPE)
                err = res.stderr.read()
                if err:
                    res_msg = err
                else:
                    res_msg = res.stdout.read()
                if not res_msg:
                    res_msg = 'processed successfully!'.encode('utf-8')

                self.my_send(res_msg)

        except Exception as e:
            self.my_send(str(e))


    def get_file(self,buffer,file_name):
        '''
        发送客户端需要下载的文件
        :param buffer:
        :param file_name:
        :return:
        '''
        if os.path.exists(file_name):
            self.my_send(buffer,file_name)
        else:
            msg = '%s does not exist'%file_name
            self.my_send(buffer,msg)


    def handle(self):
        '''
        self.request 等于conn
        self.client_address 等于客户端addr
        调用所有程序功能的入口函数
        :return:
        '''
        buffer = 1024

        if not self.auth_user(buffer): #判断是不是认证用户
            err_msg = "username or password is not correct"
            self.my_send(err_msg)
            self.request.close()
        else:
            msg = "Authorised User!"
            self.my_send(msg)

        while True: #循环接收远程用户发来的命令
            recv_info = self.my_recv(buffer).decode('utf-8')
            #客户端命令格式必须为：自定义功能函数名 函数的参数(如：excmd:ifconfig -a)

            cmd = recv_info.split(':')[0]
            param = recv_info.split(':')[1]
            # print(cmd,param)

            if hasattr(self,cmd):
                self.func = getattr(self,cmd)
                self.func(buffer,param)
            else:
                self.my_send('Command %s dose not exist!'%cmd)


if __name__ == "__main__":
    ip_port = ('127.0.0.1', 8009)
    s = socketserver.ThreadingTCPServer(ip_port,MySS)
    print("Socket_server started!")
    s.serve_forever()