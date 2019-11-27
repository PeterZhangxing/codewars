from learning_redis.redisobj import Pool
from learning_redis import  usingpool
import redis
import time

conn = redis.Redis(connection_pool=Pool)
# print(Pool)

# usingpool.using_pool()

# conn.set('fuck','you')
# res = conn.get('fuck')
# print(res)
#
# conn.set('x1','wanghuaqiang',ex=5)
# res1 = conn.get('x1')
# print(res1)
#
# time.sleep(4)
# res2 = conn.get('x1')
# print(res2)


# conn.lpush('kk',*[1,23,5,3,2,66,75,345,345,223,324,5345,234,])
#
# def list_iter(key,count=3):
#     index = 0
#     while True:
#         data_li = conn.lrange(key,index,index+count-1)
#         if not data_li:
#             return
#         index += count
#
#         for item in data_li:
#             yield item.decode('utf-8')
#
# for data in list_iter('kk'):
#     print(data)


mypip = conn.pipeline(transaction=True)
mypip.multi()

mypip.set('tt','string content')
mypip.hset('th','name','dajiba')
mypip.lpush('ll',*['ni','ma','ge','bi'])

mypip.execute()

print(conn.hgetall('th'))