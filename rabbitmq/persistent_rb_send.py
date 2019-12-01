import pika,time,sys

credentials = pika.PlainCredentials('zx2005', 'redhat')

# 使用上面定义的用户名密码，连接远程的队列服务器
connection = pika.BlockingConnection(pika.ConnectionParameters(
    "10.1.11.128",
    credentials=credentials
))

# 在tcp连接基础上，建立rabbit协议连接
channel = connection.channel()

# 申明一个不会因为服务重启，就被队列服务器删除的队列
channel.queue_declare(queue='task_queue',durable=True)

# 构建要发送的数据
message = ' '.join(sys.argv[1:]) or "Hello World! %s" % time.time()

channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # 实现队列中的消息，在队列服务重启后，不会被删除
                      )
                      )

print(" [x] Sent %r" % message)
connection.close()