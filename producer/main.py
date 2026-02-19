import json
from redis import Redis
from priority_logic import dividing_alerts_to_queues
from models import Alert
from redis_connection import get_redis_connection

# =====================================================
# GETTING DATA FROM JSON
# =====================================================

def load_data():
    try:
        with open("border_alerts.json") as file:
            data = json.load(file)
            return data
    except Exception as e:
        raise Exception(f"Could not open border_alerts.json file, Error: {str(e)}")
    
# =====================================================
# PYDANTIC VALIDATION
# =====================================================

def validate_alerts(alerts: list[dict]):
    return [Alert(**alert) for alert in alerts]

def convert_to_python_obj(alerts: list[Alert]):
    return [alert.model_dump() for alert in alerts]

# =====================================================
# REDIS UTILS 
# =====================================================

def sending_to_redis_queue(alerts: list[dict], queue_name: str, redis: Redis):
    idx = 0
    for alert in alerts:
        metadata = {"id": idx}
        redis.lpush(queue_name, json.dumps(metadata))
        redis.hset(f"Alert:{metadata['id']}", mapping=alert)
        idx += 1

# =====================================================
# MAIN FUNCTION
# =====================================================

def main(alerts, redis):
    # making the logic part
    urgent_queue, normal_queue = dividing_alerts_to_queues(alerts)

    # sending each queue to redis
    sending_to_redis_queue(urgent_queue, "urgent_queue", redis)
    sending_to_redis_queue(normal_queue, "normal_queue", redis)

# =====================================================
# RUN
# =====================================================

if __name__ == "__main__":
    alerts = load_data()
    validated_alerts = validate_alerts(alerts)
    python_obj_alerts = convert_to_python_obj(validated_alerts)

    r = get_redis_connection()
    main(python_obj_alerts, r)


# while True:
#     metadata = r.brpop("test_queue")[1]
#     metadata_str = json.loads(metadata)
#     task_id = metadata_str["id"]

#     task_data = {k.decode(): v.decode() for k, v in r.hgetall(task_id).items()}
#     print(task_data)




# metadata = {
#     "id": 123
# }

# r.lpush("test_queue", json.dumps(metadata))

# data = {
#     "person_id": 1,
#     "name": "yossi"
#     }

# r.hset(metadata["id"], mapping=data)