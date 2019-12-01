import pika,sys

credentials = pika.PlainCredentials('zx2005', 'redhat')

# 使用上面定义的用户名密码，连接远程的队列服务器
connection = pika.BlockingConnection(pika.ConnectionParameters(
    "10.1.11.128",
    credentials=credentials
))

# 在tcp连接基础上，建立rabbit协议连接
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

# 获取所有监听的组播信道
severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

# 将接收端生成的随机queue和交换器绑定，接收所有指定交换器发来的消息
for severity in severities:
    channel.queue_bind(exchange='direct_logs',queue=queue_name,routing_key=severity)

def callback(ch,method,properties,body):
    print("[x] %r:%r" % (method.routing_key, body))

channel.basic_consume(
    callback,
    queue=queue_name,
    no_ack=True
)

channel.start_consuming()