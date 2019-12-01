import pika,time

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

# 定义接收到数据后，所做的处理
def callback(ch,method,properties,body):
    print("received msg...start processing....", body)
    time.sleep(20)
    print(" [x] msg process done....", body)

# 准备开始去队列中提取数据
channel.basic_consume(
    callback, # 取到数据后调用的函数
    queue='first_queue', # 从哪个队列取数据
    no_ack=True # 不需要取完数据，还要回复给队列服务器，才删除队列服务器上的数据
)

# 开始取数据
channel.start_consuming()