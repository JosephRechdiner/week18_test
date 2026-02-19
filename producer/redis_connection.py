import redis
import os

# REDIS_HOST = os.getenv("REDIS_HOST")
# REDIS_PORT = int(os.getenv("REDIS_PORT"))
# REDIS_DB = int(os.getenv("REDIS_DB"))

def get_redis_connection():
    return redis.Redis(host="localhost", port=6379, db=0)