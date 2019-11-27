import pika

credentials = pika.PlainCredentials('zx2005', 'redhat')

# 使用上面定义的用户名密码，连接远程的队列服务器
connection = pika.BlockingConnection(pika.ConnectionParameters(
    "10.1.11.128",
    credentials=credentials
))

# 在tcp连接基础上，建立rabbit协议连接
channel = connection.channel()

# 申明要在服务器上建立的queue
channel.queue_declare(queue='first_queue')

# 发送数据到刚才建立的queue中
channel.basic_publish(
    exchange='',
    routing_key='first_queue',# 指明发送数据到哪个队列
    body='hello my lord!' # 指明发送的数据内容
)

print("sended hello my lord!")

# 关闭网络连接
connection.close()