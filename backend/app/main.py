from fastapi import FastAPI

from app.core.config import settings


app = FastAPI(
    title=settings.APP_NAME,
    description="AI-powered traffic monitoring backend",
    version=settings.APP_VERSION,
)


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
    }