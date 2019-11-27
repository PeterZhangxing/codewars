import redis

Pool = redis.ConnectionPool(
    host='10.1.1.128',
    port=6379,
    password='redhat',
    max_connections=1000,
)