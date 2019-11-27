#!/usr/bin/python3.5

import socket,subprocess

ip_port = ('127.0.0.1',8009)
buffer = 1024

udp_sev = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_sev.bind(ip_port)

print("start udp server")

while True:
    data,addr = udp_sev.recvfrom(buffer)

    res = subprocess.Popen(data.decode('utf-8'),shell=True,
                           stderr = subprocess.PIPE,
                           stdout = subprocess.PIPE,
                           stdin = subprocess.PIPE)
    err = res.stderr.read()
    if err:
        res_msg = err
    else:
        res_msg = res.stdout.read()

    if not res_msg:
        res_msg = 'processed successfully!'.encode('utf-8')

    print(len(res_msg))
    udp_sev.sendto(str(len(res_msg)).encode('utf-8'),addr)

    udp_sev.sendto(res_msg,addr)