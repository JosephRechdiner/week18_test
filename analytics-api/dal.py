from pymongo import MongoClient


class MongoDal:
# 1
    @staticmethod
    def get_alerts_by_border_and_priority(client: MongoClient):
        database = client["alerts_database"]
        collection = database["alerts_collection"]

        pipeline1 = [
            {"$match": {"priority": "URGENT"}},
            {"$group": { "_id": "$border", "count": { "$sum": 1 }}},
            {"$project": {"_id": 0}}
        ]
        pipeline2 = [
            {"$match": {"priority": "NORMAL"}},
            {"$group": {"_id": "$border", "count": { "$sum": 1 }}},
            {"$project": {"_id": 0}}
        ]
        res = []
        res.append(list(collection.aggregate(pipeline1)))
        res.append(list(collection.aggregate(pipeline2)))
        return res

# 2
    @staticmethod
    def get_top_urgent_zones(client: MongoClient):
        database = client["alerts_database"]
        collection = database["alerts_collection"]

        pipeline = [
            {"$match": {"priority": "URGENT"}},
            {"$group": {"_id": "$distance_from_fence_m", "close": { "$sum": 1 }}},
            {"$sort": {"amount": -1}},
            {"$limit": 5 }
        ]
        return list(collection.aggregate(pipeline))
# 3
    @staticmethod
    def get_distance_distribution(client: MongoClient):
        database = client["alerts_database"]
        collection = database["alerts_collection"]

        pipeline = [
            {"$match": {"priority": "URGENT"}},
            {"$group": {"_id": "$zone", "count": { "$sum": 1 }}},
            {"$sort": {"amount": -1}},
            {"$limit": 5 },
            {"$project": {"_id": 0}}
        ]
        return list(collection.aggregate(pipeline))

# 4
    @staticmethod
    def get_low_visibility_high_activity(client: MongoClient):
        database = client["alerts_database"]
        collection = database["alerts_collection"]

        pipeline = [
            {"$match": {"visibility_quality": {"$lte": 0.5}}},
            {"$project": {"_id": 0, "zone": 1}}
        ]
        return list(collection.aggregate(pipeline))

# 5
    @staticmethod
    def get_hot_zonesy(client: MongoClient):
        database = client["alerts_database"]
        collection = database["alerts_collection"]

        pipeline = [
            {"$group": {"_id": "$zone", "avg": { "$avg": "distance_from_fence_m"}}},
            {"$project": {"_id": 0, "zone": 1}}
        ]
        return list(collection.aggregate(pipeline))