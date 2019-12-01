import pika,subprocess
from rabbitmq import config

class RpcServer(object):

    def __init__(self):
        '''
        初始化接收命令的队列
        '''
        credentials = pika.PlainCredentials(config.rabbitmq_server_user, config.rabbitmq_server_passwd)
        # 使用上面定义的用户名密码，连接远程的队列服务器
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            config.rabbitmq_server_ip,
            credentials=credentials
        ))
        # 在tcp连接基础上，建立rabbit协议连接
        self.channel = self.connection.channel()
        # 声明存储客户端命令的队列
        self.channel.queue_declare(queue='rpc_queue')
        # 在向队列服务器确认数据处理完成前，只获取列表中的一个数据
        self.channel.basic_qos(prefetch_count=1)


    def run_command(self,command):
        '''
        在本服务器上执行任务，返回结果
        :param command:
        :return:
        '''
        if not command:
            res = "You must input some words!"
        else:
            res = subprocess.getoutput(command)
        return res


    def on_request(self,ch,method,props,body):
        '''
        收到命令后，调用的函数，返回结果到客户端指定的队列中
        '''
        print("received command: ",body.decode('utf-8'))
        command = body.decode('utf-8')
        response = self.run_command(command)
        ch.basic_publish(
            exchange='',
            routing_key=props.reply_to,
            properties=pika.BasicProperties(
                correlation_id=props.correlation_id,
            ),
            body=response.encode('utf-8')
        )
        # 处理完从队列中获取的数据后，通知rpc_queue删除队列中的数据
        ch.basic_ack(delivery_tag=method.delivery_tag)


    def start_process(self):
        '''
        开始接收命令，并处理
        :return:
        '''
        # 获取命令队列中的数据
        self.channel.basic_consume(self.on_request, queue='rpc_queue')
        print(" [x] Awaiting RPC requests")
        self.channel.start_consuming()


if __name__ == '__main__':

    my_rpc_server = RpcServer()
    my_rpc_server.start_process()