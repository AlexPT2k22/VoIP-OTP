from __future__ import annotations
import time
from redis.asyncio import Redis

class RateLimiter():
    def __init__(self, redis: Redis):
        self._redis = redis
        
    async def is_allowed(self, key: str, max_requests: int, window_seconds: int) -> tuple[bool, int]:
        now = time.time()
        window_start = now - window_seconds
        redis_key = f"ratelimit:{key}"
        async with self._redis.pipeline(transaction=True) as pipe:
            pipe.zremrangebyscore(redis_key, 0, window_start)
            pipe.zcard(redis_key)
            pipe.zadd(redis_key, {str(now): now})
            pipe.expire(redis_key, window_seconds + 1)
            results = await pipe.execute()

        current_count = results[1]
        if current_count >= max_requests:
            oldest_entries = await self._redis.zrange(redis_key, 0, 0, withscores=True)
            if oldest_entries:
                oldest_score = oldest_entries[0][1]
                retry_after = int(oldest_score + window_seconds - now) + 1
                return (False, max(retry_after, 0))
        else:
            return (True, 0)