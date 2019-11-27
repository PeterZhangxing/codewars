#!/usr/bin/python3.5

import socket,struct,json


def my_send(conn,msg):
    length = len(msg)
    data_len = struct.pack('i', length)
    conn.send(data_len)
    if type(msg) is str:
        conn.send(msg.encode('utf-8'))
    else:
        conn.send(msg)


def my_auth(conn,buffer):
    user_info_dic = {}
    user_info_dic['name'] = input('username: ').strip()
    user_info_dic['passwd'] = input('password: ').strip()
    user_info = json.dumps(user_info_dic).encode('utf-8')
    my_send(conn, user_info)
    auth_res_data = my_recv(conn,buffer)
    if auth_res_data.decode('utf-8') == "username or password is not correct":
        conn.close()
        print("username or password is not correct")
        return False
    else:
        print(auth_res_data)
        return True


def my_recv(conn,buffer):
    res_dsize = conn.recv(4)
    res_dsize = struct.unpack('i', res_dsize)[0]

    rev_dsize = 0
    res_data = b''
    while rev_dsize < res_dsize:
        res_data += conn.recv(buffer)
        rev_dsize = len(res_data)

    return res_data


def comm_server(conn,buffer):
    while True:
        cmd = input('>>>: ').strip()
        if not cmd: continue
        if cmd == 'quit':
            conn.close()
            exit('Quited from this programme!')

        conn.send(cmd.encode('utf-8'))

        res_data = my_recv(conn,buffer).decode('GBK')

        print('====================================== result ======================================')
        print(res_data)



if __name__ == "__main__":
    ip_port = ('127.0.0.1',8009)
    buffer = 1024

    while True:
        tcp_cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_cli.connect(ip_port)

        if not my_auth(tcp_cli,buffer):
            tcp_cli.close()
            continue

        comm_server(tcp_cli,buffer)
