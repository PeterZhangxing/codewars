#!/usr/bin/python3.5

import socket,subprocess,struct

ip_port = ('127.0.0.1',8009)
buffer = 1024
holding_num = 5

def run_command(cmd):
    res = subprocess.Popen(cmd.decode('utf-8'),
                           shell=True,
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
    return res_msg

tcp_ser = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_ser.bind(ip_port)
tcp_ser.listen(holding_num)

while True:
    conn,addr = tcp_ser.accept()
    print("recieved new connection request")

    while True:
        try:
            cmd = conn.recv(buffer)
            if not cmd:continue

            # res = subprocess.Popen(cmd.decode('utf-8'), shell=True,
            #                        stderr=subprocess.PIPE,
            #                        stdout=subprocess.PIPE,
            #                        stdin=subprocess.PIPE)
            # err = res.stderr.read()
            # if err:
            #     res_msg = err
            # else:
            #     res_msg = res.stdout.read()
            # if not res_msg:
            #     res_msg = 'processed successfully!'.encode('utf-8')

            res_msg = run_command(cmd)
            length = len(res_msg)
            data_len = struct.pack('i',length) #把数字格式化为四个字节的二进制数
            conn.send(data_len)
            conn.send(res_msg)
        except Exception as e:
            print(e)
            break