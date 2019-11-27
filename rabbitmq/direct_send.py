import pika,sys

credentials = pika.PlainCredentials('zx2005', 'redhat')

# 使用上面定义的用户名密码，连接远程的队列服务器
connection = pika.BlockingConnection(pika.ConnectionParameters(
    "10.1.11.128",
    credentials=credentials
))

# 在tcp连接基础上，建立rabbit协议连接
channel = connection.channel()

# 定义组播类型的交换器
channel.exchange_declare(exchange='direct_logs',type='direct')

# 定义要发送消息给哪个组
severity = sys.argv[1] if len(sys.argv) > 1 else 'info'

# 生成消息内容
message = ' '.join(sys.argv[2:]) or 'Hello World!'

# 发送消息到交换器
channel.basic_publish(
    exchange='direct_logs',
    routing_key=severity,
    body=message
)

print(" [x] Sent %r:%r" % (severity, message))
connection.close()