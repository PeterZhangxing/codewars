#!/usr/bin/python3.5

import socket

ip_port = ('127.0.0.1',8009)
buffer = 1024

udp_cli = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    cmd = input('>>>: ').strip()
    if not cmd:continue
    if cmd == 'quit':
        udp_cli.close()
        exit('quited from this programme!')

    udp_cli.sendto(cmd.encode('utf-8'),ip_port)

    udp_size,addr = udp_cli.recvfrom(buffer)
    answer_buffer = int(udp_size.decode('utf-8'))

    data,addr = udp_cli.recvfrom(answer_buffer)
    # data,addr = udp_cli.recvfrom(buffer)
    print(data.decode('gbk'))