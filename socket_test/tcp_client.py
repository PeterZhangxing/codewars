#!/usr/bin/python3.5

import socket
import struct

ip_port = ('127.0.0.1',8009)
buffer = 1024

tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_client.connect(ip_port)

while True:
    cmd = input(">>>: ")
    if not cmd:continue
    if cmd == "quit" or cmd == "exit" or cmd == "Q":
        tcp_client.close()
        exit("quited from this programme")

    tcp_client.send(cmd.encode('utf-8'))

    res_len = tcp_client.recv(4)
    res_len = struct.unpack('i', res_len)[0]
    print(res_len)

    res_data = b''
    read_len = 0
    if res_len <= buffer:
        res_data = tcp_client.recv(res_len)
    else:
        while read_len < res_len:
            if res_len - read_len >= buffer:
                res_data += tcp_client.recv(buffer)
            else:
                res_data += tcp_client.recv(res_len-read_len)
            read_len = len(res_data)

    print(res_data)