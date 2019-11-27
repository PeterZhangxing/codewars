import socketserver
import hmac
import os

class MyServer(socketserver.BaseRequestHandler):
    __pre_key = b'123abc'

    def handle(self):
        id_res = self.identify_cli()
        print(id_res)
        if id_res:
            self.request.send(b'hello')
        else:
            self.request.send("MLGB,fucking off!".encode('utf-8'))

    def build_id(self):
        id_msg = os.urandom(32)
        self.request.send(id_msg)
        h_res = hmac.new(MyServer.__pre_key,id_msg)
        return h_res.digest()

    def identify_cli(self):
        svr_msg = self.build_id()
        cli_msg = self.request.recv(1024)
        if cli_msg == svr_msg:
            return True
        return False

if __name__ == '__main__':
    ip_port = ("127.0.0.1",8089)
    mys_obj = socketserver.ThreadingTCPServer(
        ip_port,
        MyServer
    )
    print('start socket_server on %s:%s'%(ip_port[0],ip_port[1]))
    mys_obj.serve_forever()