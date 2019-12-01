import pika,uuid
from rabbitmq import config

class RpcClient(object):

    def __init__(self):
        '''
        完成队列服务器连接初始化，生成用于客户端接收数据的队列，
        并使其处于准备接收服务器返回数据的状态。
        '''
        credentials = pika.PlainCredentials(config.rabbitmq_server_user, config.rabbitmq_server_passwd)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            config.rabbitmq_server_ip,
            credentials=credentials))
        self.channel = self.connection.channel()

        # 生成用于接收服务器消息的随机队列
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        # 准备接收服务器端的返回结果
        self.channel.basic_consume(
            self.on_response,
            no_ack=True,
            queue=self.callback_queue
        )


    def on_response(self,ch,method,props,body):
        '''
        定义接收到服务器的返回信息后，对数据执行的操作
        '''
        if self.corr_id == props.correlation_id:
            self.response = body


    def call(self,command):
        '''
        从命令发送队列发送命令到服务器端，
        并从自己生成的随机队列中收取执行结果。
        '''
        self.response = None
        # 为客户端发送的信息和服务器端将返回的信息生成唯一标识符
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',# 服务端定义的用于接收命令的队列
            properties=pika.BasicProperties(
                reply_to=self.callback_queue, # 告诉对端返回的消息放入哪个队列
                correlation_id=self.corr_id, # 告诉对端，返回的消息需要携带的id
            ),
            body=command,
        )

        while self.response is None:
            # 检查自己生成的队列里有没有新消息,但不会阻塞,有新消息就消费
            self.connection.process_data_events()

        return self.response


if __name__ == '__main__':

    my_rpc_client = RpcClient()

    while True:
        command = input("command: ") or "ipconfig /all"
        if command == "exit":
            break
        res = my_rpc_client.call(command)
        print(" [.] Got %s" %res.decode('utf-8'))

    print("Exit from client process.")