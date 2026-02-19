import redis
import os

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT"))
REDIS_DB = int(os.getenv("REDIS_DB"))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

