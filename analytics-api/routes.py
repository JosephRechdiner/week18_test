from fastapi import APIRouter, Request, Depends, HTTPException
from redis import Redis
from dal import MongoDal

# =====================================================
# DEPENDENCIES
# =====================================================

def get_mongo_manager(request: Request):
    return request.app.state.mongo_manager

def get_redis_connection(request: Request):
    return request.app.state.redis_connection

# =====================================================
# ROUTES
# =====================================================

router = APIRouter()

# 1
@router.get("/analytics/alerts-by-border-and-priority")
def get_alerts_by_border_and_priority(redis_connection: Redis = Depends(get_redis_connection), mongo_manager = Depends(get_mongo_manager)):
    client = mongo_manager.get_client()
    alerts = redis_connection.get("alerts-by-border-and-priority")
    if alerts:
        return alerts
    
    redis_connection.setex("alerts-by-border-and-priority", time=300)
    alerts = MongoDal.get_alerts_by_border_and_priority(client)
    if not alerts:
        raise HTTPException(status_code=404, detail="Not Found")
    return alerts

# 2
@router.get("/analytics/top-urgent-zones")
def get_top_urgent_zones(redis_connection = Depends(get_redis_connection), mongo_manager = Depends(get_mongo_manager)):
    client = mongo_manager.get_client()
    alerts = redis_connection.get("top-urgent-zones")
    if alerts:
        return alerts
    
    redis_connection.setex("top-urgent-zones", time=300)
    alerts = MongoDal.get_top_urgent_zones(client)
    if not alerts:
        raise HTTPException(status_code=404, detail="Not Found")
    return alerts

# 3
@router.get("/analytics/distance-distribution")
def get_distance_distribution(redis_connection = Depends(get_redis_connection), mongo_manager = Depends(get_mongo_manager)):
    client = mongo_manager.get_client()
    alerts = redis_connection.get("distance-distribution")
    if alerts:
        return alerts
    
    redis_connection.setex("distance-distribution", time=300)
    alerts = MongoDal.get_distance_distribution(client)
    if not alerts:
        raise HTTPException(status_code=404, detail="Not Found")
    return alerts

# 4
@router.get("/analytics/low-visibility-high-activity")
def get_low_visibility_high_activity(redis_connection = Depends(get_redis_connection), mongo_manager = Depends(get_mongo_manager)):
    client = mongo_manager.get_client()
    alerts = redis_connection.get("low-visibility-high-activity")
    if alerts:
        return alerts
    
    redis_connection.setex("low-visibility-high-activity", time=300)
    alerts = MongoDal.get_low_visibility_high_activity(client)
    if not alerts:
        raise HTTPException(status_code=404, detail="Not Found")
    return alerts

# 5
@router.get("/analytics/hot-zones")
def get_hot_zonesy(redis_connection = Depends(get_redis_connection), mongo_manager = Depends(get_mongo_manager)):
    client = mongo_manager.get_client()
    alerts = redis_connection.get("hot-zones")
    if alerts:
        return alerts
    
    redis_connection.setex("hot-zones", time=300)
    alerts = MongoDal.get_hot_zonesy(client)
    if not alerts:
        raise HTTPException(status_code=404, detail="Not Found")
    return alerts

