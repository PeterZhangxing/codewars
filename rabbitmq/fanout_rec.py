import pika

credentials = pika.PlainCredentials('zx2005', 'redhat')

# 使用上面定义的用户名密码，连接远程的队列服务器
connection = pika.BlockingConnection(pika.ConnectionParameters(
    "10.1.1.128",
    credentials=credentials
))

# 在tcp连接基础上，建立rabbit协议连接
channel = connection.channel()

# 申明一个广播类型的交换器
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# 不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue # 取得随机队列的名字

# 使得队列接收交换器发来的消息
channel.queue_bind(exchange='logs', queue=queue_name)

# 从自己申明的队列接收广播消息
def callback(ch, method, properties, body):
    print(" [x] %r" % body)

# 开始从队列中取出数据
channel.basic_consume(callback, queue=queue_name,no_ack=True)
channel.start_consuming()