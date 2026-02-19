import json

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
# GETTING DATA FROM JSON
# =====================================================

data = load_data()

# while True:
#     metadata = r.brpop("test_queue")[1]
#     metadata_str = json.loads(metadata)
#     task_id = metadata_str["id"]

#     task_data = {k.decode(): v.decode() for k, v in r.hgetall(task_id).items()}
#     print(task_data)




metadata = {
    "id": 123
}

r.lpush("test_queue", json.dumps(metadata))

data = {
    "person_id": 1,
    "name": "yossi"
    }

r.hset(metadata["id"], mapping=data)