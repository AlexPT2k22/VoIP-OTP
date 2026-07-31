from __future__ import annotations
from redis.asyncio import Redis
from app.config import settings
from app.repository.base import BaseOTPRepository
from app.schemas.otp import OTPRecord

class RedisOTPRepository(BaseOTPRepository):
    def __init__(self, redis: Redis):
        self._redis = redis
        
    def _key(self, phone: str) -> str:
        return f"otp:{phone}"
    
    async def save(self, record: OTPRecord) -> None:
        data = record.model_dump_json()
        await self._redis.setex(
        self._key(record.phone),
        settings.otp_ttl_seconds,
        data,
    )
        
    async def get(self, phone: str) -> OTPRecord | None:
        data = await self._redis.get(self._key(phone))
        if data is None:
            return None
        return OTPRecord.model_validate_json(data)
        
    async def delete(self, phone: str) -> None:
        await self._redis.delete(self._key(phone))
        
    async def exists(self, phone: str) -> bool:
        return await self._redis.exists(self._key(phone)) > 0