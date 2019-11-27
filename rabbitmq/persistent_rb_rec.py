import pika,time

credentials = pika.PlainCredentials('zx2005', 'redhat')

# 使用上面定义的用户名密码，连接远程的队列服务器
connection = pika.BlockingConnection(pika.ConnectionParameters(
    "10.1.11.128",
    credentials=credentials
))

# 在tcp连接基础上，建立rabbit协议连接
channel = connection.channel()

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(15)
    print(" [x] Done")

    print("method.delivery_tag", method.delivery_tag)
    # method.delivery_tag 1

    # 取完消息，发送确认给队列服务器，才删除队列中的数据
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(
    callback,
    queue='task_queue',
    no_ack=False # 需要确认才，删除队列服务器上的数据
    )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()