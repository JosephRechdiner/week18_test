from contextlib import asynccontextmanager
from fastapi import FastAPI
from routes import router
from mongo_connection import MongoManager
from redis_connection import get_redis_connection

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.mongo_manager = MongoManager()
    app.state.redis_connection = get_redis_connection()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)