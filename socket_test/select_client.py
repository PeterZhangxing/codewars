import select
import socket

class HttpRequest(object):
     '''
     将socket对象封装起来，使其包括请求的主机，和回调函数
     '''
     def __init__(self,sk,host,callback):
         self.socket = sk
         self.host = host
         self.callback = callback

     def fileno(self):
         '''
         select监控的对象必须有fileno方法，并且能返回文件描述符
         :return:
         '''
         return self.socket.fileno()


class HttpResponse(object):
    '''
    格式化返回的http报文,分别获取响应报文的header和body
    '''
    def __init__(self,recv_data):
        self.recv_data = recv_data
        self.header_gen_list = []
        self.header_dict = {}
        self.body = None
        self.initialize()

    def initialize(self):
        headers,body = self.recv_data.split(b'\r\n\r\n',1)
        self.body = body
        header_list = headers.split(b'\r\n')
        for header in header_list:
            h_str = header.decode('utf-8')
            res = h_str.split(':',1)
            if len(res) == 2:
                self.header_dict[res[0]] = res[1]
            elif len(res) == 1:
                self.header_gen_list.append(res[0])


class AsyncRequest(object):
    '''
    create tcp connection and keep checking
    whether there is any thing happened during
    this process
    '''
    def __init__(self):
        # for checking whether the socket_obj has received any data
        self.conn = []
        # for checking whether the tcp connection between client and server has been created
        self.connection = []

    def add_request(self,host,callback):
        '''
        客户端创建不等待的IO的socket请求
        :param host:
        :param callback:
        :return:
        '''
        try:
            sk = socket.socket()
            sk.setblocking(False)
            sk.connect((host,80,))
        except BlockingIOError as e:
            pass
        request_obj = HttpRequest(sk,host,callback)
        self.conn.append(request_obj)
        self.connection.append(request_obj)

    def run(self):
        while True:
            # 每隔0.05s扫描以下列表中的socket对象的文件描述符是不是有io活动，有就返回被监控的对象
            # 连接成功，会返回对象到w_li中，收到数据会返回对象到r_li
            r_li,w_li,e_li = select.select(self.conn,self.connection,self.conn,0.05)
            for w in w_li:
                print(w.host,'connected...')
                tpl = "GET / HTTPS/1.0\r\nHost:%s\r\n\r\n" % (w.host,)
                w.socket.send(tpl.encode('utf-8'))
                # 连接成功就不需要再监控是不是连接成功了
                self.connection.remove(w)

            for r in r_li:
                # 循环接收所有的数据，收到空数据时，说明已经收到所有数据，终止循环
                recv_data = bytes()
                while True:
                    try:
                        chunck = r.socket.recv(1024)
                        recv_data += chunck
                    except Exception as e:
                        break

                response_obj = HttpResponse(recv_data)

                # 执行封装在某个socket对象中的回调函数
                r.callback(response_obj)
                r.socket.close()
                # 完成收取数据后，不再监控该socket对象是不是到数据
                self.conn.remove(r)

            # 如果所有被监控对象都已经完成收取数据，就不用再继续监控io文件描述符的动作
            if len(self.conn) == 0:
                break


if __name__ == '__main__':

    def f1(response):
        print('保存到文件', response.header_dict,response.header_gen_list)

    def f2(response):
        print('保存到数据库', response.header_dict,response.header_gen_list)

    url_li = [
        {'host':'www.baidu.com','callback': f1},
        {'host':'cn.bing.com','callback': f2},
        {'host':'www.cnblogs.com','callback': f2},
    ]

    my_req_obj = AsyncRequest()
    for item in url_li:
        my_req_obj.add_request(item['host'],item['callback'])

    my_req_obj.run()