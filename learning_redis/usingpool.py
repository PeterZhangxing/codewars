from learning_redis.redisobj import Pool
import redis

def using_pool():
    conn = redis.Redis(connection_pool=Pool)
    print(Pool)
    return None