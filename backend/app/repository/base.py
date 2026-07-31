from __future__ import annotations
from abc import ABC, abstractmethod
from app.schemas.otp import OTPRecord

class BaseOTPRepository(ABC):
    @abstractmethod
    async def save(self, otp: OTPRecord) -> None:
        pass

    @abstractmethod
    async def get(self, phone: str) -> OTPRecord | None:
        pass

    @abstractmethod
    async def exists(self, phone: str) -> bool:
        pass

    @abstractmethod
    async def delete(self, phone: str) -> None:
        pass