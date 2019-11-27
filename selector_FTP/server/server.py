#/usr/bin/python3.5

import os,time
import socket,selectors

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class SelFtp(object):

    def __init__(self):
        self.dic = {}
        self.sel = selectors.DefaultSelector()
        self.create_sock()
        self.handle()


    def create_sock(self):
        server = socket.socket()
        server.bind(('127.0.0.1',8009))
        server.listen(5)
        server.setblocking(False)
        self.sel.register(server,selectors.EVENT_READ,self.accept)
        print('start FTP service')


    def handle(self):
        while True:
            events = self.sel.select()
            for key,mask in events:
                callback = key.data # 监听到有I/o数据产生的对象，对应的注册的函数
                callback(key.fileobj,mask) # 把产生I/O的对象传递进自己注册的函数中，执行函数


    def accept(self,sock,mask):
        conn,addr = sock.accept()
        conn.setblocking(False) # 使得连接不会传输完数据才释放
        self.sel.register(conn,selectors.EVENT_READ,self.read)

        self.dic[conn] = {}


    def read(self,conn,mask):
        try:

            if not self.dic[conn]:
                data = conn.recv(1024)
                cmd,filename,filesize = data.decode('utf-8').split('|')
                self.dic = {conn:{'cmd':cmd,'filename':filename,'filesize':int(filesize)}}

                if cmd == 'put':
                    conn.sendall("OK".encode('utf-8'))
                    self.dic[conn]['hasrecv'] = 0

                if cmd == 'get':
                    file = os.path.join(BASE_DIR,"download",filename)
                    self.dic[conn]['hassend'] = 0
                    if os.path.exists(file):
                        file_ssize = os.path.getsize(file)
                        send_info = '%s|%s'%('yes',file_ssize)
                        conn.sendall(send_info.encode('utf-8'))
                    else:
                        send_info = '%s|%s'%('no',0)
                        conn.sendall(send_info.encode('utf-8'))
            else:
                if self.dic[conn].get('cmd',None):
                    cmd = self.dic[conn].get('cmd')
                    if hasattr(self,cmd):
                        func = getattr(self,cmd)
                        func(conn)
                    else:
                        print('wrong command')
                        conn.close()

        except Exception as e:
            print('error: ',e)


    def put(self,conn):
        filename = self.dic[conn].get('filename')
        filesize = self.dic[conn].get('filesize')
        path = os.path.join(BASE_DIR,"upload",filename)
        recv_data = conn.recv(1024)
        self.dic[conn]['hasrecv'] += len(recv_data)

        with open(path,'ab') as f:
            f.write(recv_data)
        if filesize == self.dic[conn]['hasrecv']:
            if conn in self.dic.keys():
                self.dic[conn] = {}
            print("%s upload completely"%filename)


    def get(self,conn):
        filename = self.dic[conn].get('filename')
        path = os.path.join(BASE_DIR, "download", filename)
        filesize = os.path.getsize(path)
        cli_mes = conn.recv(1024).decode('utf-8')

        if cli_mes.upper() == "OK":
            with open(path,'rb') as f:
                if self.dic[conn]['hassend'] < filesize:
                    f.seek(self.dic[conn]['hassend'])
                    data = f.read(1024)
                    self.dic[conn]['hassend'] += len(data)
                    conn.sendall(data)
                else:
                    if conn in self.dic.keys():
                        self.dic[conn] = {}
                    print("%s download completely" % filename)



if __name__ == "__main__":
    SelFtp()