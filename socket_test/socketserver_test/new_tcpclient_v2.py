#!/usr/bin/python3.5

import socket,struct,json,os


def my_send(conn,msg):
    length = len(msg)
    data_len = struct.pack('i', length)
    conn.send(data_len)
    if type(msg) is str:
        conn.send(msg.encode('utf-8'))
    else:
        conn.send(msg)


def my_recv(conn,buffer):
    res_dsize = conn.recv(4)
    res_dsize = struct.unpack('i', res_dsize)[0]
    rev_dsize = 0
    res_data = b''
    while rev_dsize < res_dsize:
        res_data += conn.recv(buffer)
        rev_dsize = len(res_data)
    return res_data


def my_recv_file(conn,buffer,file_name):
    try:
        if not os.path.isfile(file_name):
            res_dsize = conn.recv(4)
            res_dsize = struct.unpack('i', res_dsize)[0]
            if res_dsize == 0:
                return 'file %s is null'%file_name
            with open(file_name,'wb') as f:
                rev_dsize = 0
                res_data = b''
                while rev_dsize < res_dsize:
                    tmp_data = conn.recv(buffer)
                    f.write(tmp_data)
                    rev_dsize += len(tmp_data)
            return 'file %s downloaded'%file_name
        else:
            return 'file %s already exists' % file_name
    except Exception as e:
        return str(e)


def my_send_file(conn,buffer,file_name):
    try:
        if os.path.isfile(file_name):
            length = len(file_name)
            if length == 0:
                return 'file %s is null' % file_name
            data_len = struct.pack('i', length)
            conn.send(data_len)
            with open(file_name, 'rb') as f:
                for line in f.read():
                    conn.send(line)
            return 'file %s uploaded' % file_name
        else:
            return 'file %s dose not exist' % file_name
    except Exception as e:
        return str(e)


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
        print(auth_res_data.decode('utf-8'))
        return True


def comm_server(conn,buffer):
    while True:
        cmd = input('>>>: ').strip()
        if not cmd: continue
        if cmd == 'quit':
            conn.close()
            exit('Quited from this programme!')
        elif cmd.startswith('get'):# get test.txt
            my_send(conn,cmd.encode('utf-8'))
            get_file_name = cmd.split()[1]
            get_res = my_recv_file(conn, buffer, get_file_name)
            print(get_res)
        elif cmd.startswith('send'):# send test.txt
            my_send(conn, cmd.encode('utf-8'))
            # 如果服务器端同意上传，就会发来OK,否则发错误消息，如"file already exist"
            if my_recv(conn,buffer).decode('utf-8') == 'OK':
                send_file_name = cmd.split()[1]
                send_res = my_send_file(conn, buffer, send_file_name)
                print(send_res)
            else:
                print(my_recv(conn,buffer).decode('utf-8'))
        else:
            my_send(conn,cmd.encode('utf-8'))
            res_data = my_recv(conn,buffer).decode('GBK')
            print('='*20 + ' result ' + '='*20)
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