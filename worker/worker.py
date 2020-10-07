import redis
import os
from dotenv import load_dotenv
load_dotenv()

host = os.environ.get("REDIS_HOST")
port = os.environ.get("REDIS_PORT")

r = redis.Redis(host=host, port=port, db=0)

def fib(index):
    if index < 2:
        return 1
    return fib(index - 1) + fib(index - 2)

listener = r.pubsub()
listener.subscribe('index')
for new_msg in listener.listen():
    print(new_msg['data'])
    r.hset('index', int(new_msg['data']), fib(int(new_msg['data'])))
