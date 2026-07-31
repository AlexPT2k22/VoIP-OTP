from __future__ import annotations
import secrets
import hmac
import hashlib

def generate_otp(length: int) -> str:
    otp = []
    for _ in range(length):
        otp.append(str(secrets.randbelow(10)))
    
    return "".join(otp)

def hash_otp(otp: str, phone: str) -> str:
    return hmac.new(key= phone.encode(), msg=otp.encode(), digestmod=hashlib.sha256).hexdigest()

def verify_otp(otp: str, phone: str, stored_hash: str) -> bool:
    expected = hash_otp(otp, phone)
    return hmac.compare_digest(expected, stored_hash)