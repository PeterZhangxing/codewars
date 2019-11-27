import hmac
import socket

ip_port = ("127.0.0.1",8089)
cli_socket = socket.socket()
cli_socket.connect(ip_port)

def send_id(pre_key,rec_msg):
    h_obj = hmac.new(pre_key,rec_msg)
    h_res = h_obj.digest()
    cli_socket.send(h_res)
    return cli_socket.recv(1024)

pre_key = b'123abc'
rec_msg = cli_socket.recv(1024)

svr_msg = send_id(pre_key,rec_msg)
print(svr_msg)