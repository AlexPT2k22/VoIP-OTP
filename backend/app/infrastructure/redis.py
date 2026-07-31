from __future__ import annotations
from redis.asyncio import Redis, ConnectionPool
import structlog
from app.config import settings

_redis_pool: ConnectionPool | None = None

async def get_redis() -> Redis:
    if _redis_pool is None:
        await init_redis()
    return Redis(connection_pool=_redis_pool)

async def init_redis():
    global _redis_pool
    _redis_pool = ConnectionPool.from_url(settings.redis_url, max_connections=settings.redis_max_connections, decode_responses=True)
    redis = Redis(connection_pool=_redis_pool)
    await redis.ping()
    logger = structlog.get_logger()
    logger.info("Connected to Redis")

async def close_redis():
    global _redis_pool
    if _redis_pool is not None:
        await _redis_pool.disconnect()
        _redis_pool = None
        logger = structlog.get_logger()
        logger.info("Disconnected from Redis")