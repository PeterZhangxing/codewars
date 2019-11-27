import pika,sys

credentials = pika.PlainCredentials('zx2005', 'redhat')

# 使用上面定义的用户名密码，连接远程的队列服务器
connection = pika.BlockingConnection(pika.ConnectionParameters(
    "10.1.11.128",
    credentials=credentials
))

# 在tcp连接基础上，建立rabbit协议连接
channel = connection.channel()

# 申明通过字符串匹配，来确定发送数据到哪个队列的交换器
channel.exchange_declare(exchange='topic_logs',type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(
        exchange='topic_logs',
        queue=queue_name,
        routing_key=binding_key)

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(
    callback,
    queue=queue_name,
    no_ack=True)

channel.start_consuming()