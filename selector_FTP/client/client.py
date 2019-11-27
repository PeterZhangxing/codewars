#/usr/bin/python3.5

import os,time,sys
import socket

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class FtpClient(object):

    def __init__(self):
        self.ser_ip = sys.argv[1]
        self.ser_port = int(sys.argv[2])
        self.ser_sock_add = (self.ser_ip,self.ser_port)
        self.conn_server()
        self.communicating()


    def conn_server(self):
        self.client = socket.socket()
        self.client.connect(self.ser_sock_add)


    def communicating(self):
        while True:
            cmd = input(">>>: ")
            if not cmd: continue
            if cmd == "quit" or cmd == "exit" or cmd == "Q":
                self.client.close()
                exit("quited from this programme")
            else:
                FtpCmd,filename =  cmd.split()
                if hasattr(self,FtpCmd):
                    func = getattr(self,cmd)
                    func(filename)
                else:
                    print('wrong command')


    def put(self,filename):
        path = os.path.join(BASE_DIR,filename)
        if os.path.isfile(path):
            cmd = 'put'
            filesize = os.path.getsize(path)
            meta_data = "%s|%s|%s"%(cmd,filename,filesize)
            self.client.sendall(meta_data.encode('utf-8'))
            ser_msg = self.client.recv(1024).decode('utf-8')
            if ser_msg.upper() == "OK":
                has_send = 0
                with open(path,'rb') as f:
                    while has_send < filesize:
                        file_content = f.read(1024)
                        has_send += len(file_content)
                        self.client.sendall(file_content)
                        percentage = int(float(has_send) / float(filesize) * 100)
                        sys.stdout.write("%s%% %s\r" % (percentage, '#' * percentage))
                        sys.stdout.flush()
                print("Finish uploading file %s"%filename)
            else:
                print("Unkown error!")


    def get(self,filename):
        path = os.path.join(BASE_DIR, filename)
        filesize = 0
        cmd = 'get'
        meta_data = "%s|%s|%s" % (cmd, filename, filesize)
        self.client.sendall(meta_data.encode('utf-8'))

        ser_msg = self.client.recv(1024).decode('utf-8')
        if ser_msg.split('|')[0].lower() == 'yes':
            ser_filesize = int(ser_msg.split('|')[1])
            self.client.sendall("OK".encode('utf-8'))
            has_recv = 0
            with open(path,'ab') as f:
                while has_recv < ser_filesize:
                    data = self.client.recv(1024)
                    f.write(data)
                    has_recv += len(data)
                    percentage = int(float(has_recv) / float(ser_filesize) * 100)
                    sys.stdout.write("%s%% %s\r" % (percentage, '#' * percentage))
                    sys.stdout.flush()
            print("Finish downloading file %s" % filename)
        elif ser_msg.split('|')[0].lower() == 'no':
            print("%s does not exists"%filename)
        else:
            print("Unkown error!")


if __name__ == "__main__":
    FtpClient()