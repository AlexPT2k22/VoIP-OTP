from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    
    redis_url: str = "redis://localhost:6379/0"
    redis_max_connections: int = 20
    twilio_account_sid: str = ""
    twilio_auth_token: str = ""
    twilio_phone_number: str = ""
    otp_length: int = 6
    otp_ttl_seconds: int = 300
    otp_max_attempts: int = 3
    otp_resend_cooldown_seconds: int = 60
    rate_limit_max_requests: int = 3
    rate_limit_window_seconds: int = 300
    api_prefix: str = "/api/v1"
    debug: bool = False
    app_name: str = "VoIP OTP"
    app_version: str = "0.0.1"
    @property
    def twilio_configured(self) -> bool:
        return bool(self.twilio_account_sid and self.twilio_auth_token and self.twilio_phone_number)


settings = Settings()