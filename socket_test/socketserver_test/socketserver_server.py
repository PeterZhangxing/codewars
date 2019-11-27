#!/usr/bin/python3.5

import socketserver,subprocess,struct,json

user_info = {'zx':'123','honda':'abcd','toyota':'redhat'}

class MySS(socketserver.BaseRequestHandler):

    def my_send(self,msg):
        length = len(msg)
        data_len = struct.pack('i', length)
        self.request.send(data_len)
        if type(msg) is str:
            self.request.send(msg.encode('utf-8'))
        else:
            self.request.send(msg)

    def auth_user(self):
        recv_uinfo_size = self.request.recv(4)
        res_dsize = struct.unpack('i', recv_uinfo_size)[0] #接收认证信息的大小

        recv_uinfo = self.request.recv(res_dsize) #接收客户端的用户名密码
        recv_uinfo = recv_uinfo.decode('utf-8')
        uinfo = json.loads(recv_uinfo) #{'name':'zx','passwd':'123'}

        if uinfo['name'] in user_info.keys():
            if uinfo['passwd'] == user_info[uinfo['name']]:
                print('Authorised!')
                return True
            else:
                print("password is not correct")
                return False
        else:
            print('user dose not exist')
            return False

    def handle(self):
        '''
        self.request 等于conn
        self.client_address 等于客户端addr
        '''
        buffer = 1024

        if not self.auth_user():
            err_msg = "username or password is not correct"
            # length = len(err_msg)
            # data_len = struct.pack('i', length)
            # self.request.send(data_len)
            # self.request.send(err_msg.encode('utf-8'))
            self.my_send(err_msg)
            self.request.close()
        else:
            msg = "Authorised User!"
            # length = len(msg)
            # data_len = struct.pack('i', length)
            # self.request.send(data_len)
            # self.request.send(msg.encode('utf-8'))
            self.my_send(msg)

        while True:
            try:
                cmd = self.request.recv(buffer)
                if not cmd: continue

                res = subprocess.Popen(cmd.decode('utf-8'), shell=True,
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

                # length = len(res_msg)
                # data_len = struct.pack('i', length)
                # self.request.send(data_len)
                # self.request.send(res_msg)

                self.my_send(res_msg)

            except Exception as e:
                print(e)
                self.my_send(res_msg)
                break

if __name__ == "__main__":
    ip_port = ('127.0.0.1', 8009)
    s = socketserver.ThreadingTCPServer(ip_port,MySS)
    print("Socket_server started!")
    s.serve_forever()
