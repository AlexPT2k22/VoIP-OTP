from __future__ import annotations
from pydantic import BaseModel, Field
import time

class OTPRecord(BaseModel):
    created_at: float = Field(default_factory=time.time)
    phone: str = Field(pattern=r"^\+[1-9]\d{7,14}$")
    channel: str = Field(pattern=r"^(sms|voice)$")
    attempts: int = Field(default=0)
    otp_hash: str


class SendOTPRequest(BaseModel):
    phone: str = Field(pattern=r"^\+[1-9]\d{7,14}$", examples=["+351912345678"])
    channel: str = Field(default="sms", pattern=r"^(sms|voice)$")

class VerifyOTPRequest(BaseModel):
    phone: str = Field(pattern=r"^\+[1-9]\d{7,14}$")
    code: str = Field(pattern=r"^\d{6}$") # 6 digits
    
class SendOTPResponse(BaseModel):
    message: str
    phone: str
    channel: str
    expires_in_seconds: int
    
class VerifyOTPResponse(BaseModel):
    message: str
    verified: bool