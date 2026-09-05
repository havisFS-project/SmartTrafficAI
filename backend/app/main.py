from fastapi import FastAPI

from app.api.cameras import router as cameras_router
from app.api.traffic import router as traffic_router
from app.api.alerts import router as alerts_router
from app.api.predictions import router as predictions_router
from app.core.config import settings
from app.db.mongodb import get_client

app = FastAPI(
    title=settings.APP_NAME,
    description="AI-powered traffic monitoring backend",
    version=settings.APP_VERSION,
)

app.include_router(cameras_router)
app.include_router(traffic_router)
app.include_router(alerts_router)
app.include_router(predictions_router)

@app.get("/")
async def root():
    return {
        "message": "SmartTrafficAI API is running",
        "version": settings.APP_VERSION,
    }


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": "backend",
        "debug": settings.DEBUG,
    }

@app.get("/health/database")
async def database_health():
    try:
        client = get_client()

        client.admin.command("ping")

        return {
            "status": "ok",
            "database": "connected",
        }

    except Exception as error:
        return {
            "status": "error",
            "database": "disconnected",
            "detail": str(error),
        }