from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from aioredis import Redis
from app.core.config import settings

async def init_redis():
    redis = Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        encoding="utf8",
        decode_responses=True
    )
    FastAPICache.init(
        RedisBackend(redis),
        prefix="foodapp-cache:"
    )