from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import structlog
from app.config import settings
from app.api.router import router as api_router
from app.infrastructure.redis import get_redis, close_redis

logger = structlog.get_logger()

@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:
    logger = structlog.get_logger()
    logger.info("Starting application")
    yield
    await close_redis()
    logger.info("Stopping application")

def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name, version=settings.app_version, lifespan=lifespan)
    app.include_router(api_router, prefix=settings.api_prefix)
    return app

app = create_app()

@app.get("/health")
async def health_check() -> JSONResponse:
    try:
        r = await get_redis()
        await r.ping()
        redis_ok = True
        return JSONResponse(content={"status": "healthy",
                                     "redis": redis_ok,
                                     "twilio_configured": settings.twilio_configured}, status_code=200)
    except Exception as e:
        redis_ok = False
        logger.error("Health check failed", exc_info=e)
        return JSONResponse(content={"status": "unhealthy",
                                     "redis": redis_ok,
                                     "twilio_configured": settings.twilio_configured}, status_code=503)