from redis import Redis
from mongo_connection import MongoManager, insert_to_mongo
from redis_connection import get_redis_connection
import json

# =====================================================
# MAIN FUNCTION
# =====================================================

def main(redis: Redis, mongo_manager: MongoManager):
    client = mongo_manager.get_client()
    while True:
        _, metadata = redis.brpop("urgent_queue")
        if not metadata:
            break
        metadata_str = json.loads(metadata)
        alert_id = metadata_str["id"]
        alert_data = r.hgetall(f'Alert:{alert_id}')
        alert_data = {k.decode(): v.decode() for k, v in alert_data.items()}
        insert_to_mongo(alert_data, client)

    while True:
        _, metadata = redis.brpop("normal_queue")
        if not metadata:
            break
        metadata_str = json.loads(metadata)
        alert_id = metadata_str["id"]
        alert_data = r.hgetall(f'Alert:{alert_id}')
        alert_data = {k.decode(): v.decode() for k, v in alert_data.items()}
        insert_to_mongo(alert_data, client)

# =====================================================
# RUN
# =====================================================

if __name__ == "__main__":
    mongo_manager = MongoManager()
    r = get_redis_connection()

    main(r, mongo_manager)