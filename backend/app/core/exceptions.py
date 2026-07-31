from __future__ import annotations
from fastapi import HTTPException, status

class RateLimitedExceeded(HTTPException):
    def __init__(self, retry_after: int):
        super().__init__(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=f"Too many requests. Retry after {retry_after} seconds.", headers={"Retry-After": str(retry_after)})
        
class OTPNotFound(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail="No OTP found for this phone number. Request a new one.")
        
class OTPInvalid(HTTPException):
    def __init__(self, remaining_attemps: int):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid OTP. {remaining_attemps} attempts remaining.")
        
class OTPExpired(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_410_GONE, detail="OTP has expired. Request a new one.")
        
class TwilioNotConfigured(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Notification service not configured.")
        
class InvalidPhoneNumber(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail="Invalid phone number. Use E.164 format (e.g. +351912345678).")