import pika,sys

credentials = pika.PlainCredentials('zx2005', 'redhat')

# 使用上面定义的用户名密码，连接远程的队列服务器
connection = pika.BlockingConnection(pika.ConnectionParameters(
    "10.1.1.128",
    credentials=credentials
))

# 在tcp连接基础上，建立rabbit协议连接
channel = connection.channel()

# 发送端只需要申明交换器
channel.exchange_declare(exchange='logs',exchange_type='fanout')

# 生成要广播的消息
message = ' '.join(sys.argv[1:]) or "info: Hello World!"

# 发送消息到交换器而不是队列
channel.basic_publish(
    exchange='logs',
    routing_key='',
    body=message
)

print(" [x] Sent %r" % message)

connection.close()