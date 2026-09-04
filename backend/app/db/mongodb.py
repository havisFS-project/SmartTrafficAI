from pymongo import MongoClient

from app.core.config import settings


def get_client() -> MongoClient:
    if not settings.MONGODB_URL:
        raise RuntimeError(
            "MONGODB_URL is not configured."
        )

    return MongoClient(
        settings.MONGODB_URL,
        serverSelectionTimeoutMS=5000,
    )