from datetime import datetime

from fastapi import APIRouter, Query

from app.core.config import settings
from app.db.mongodb import get_client
from app.schemas.alert import AlertCreate


router = APIRouter(
    prefix="/api/alerts",
    tags=["Alerts"],
)


def get_collection():
    client = get_client()
    database = client[settings.DATABASE_NAME]

    return database["alerts"]


@router.get("/")
async def get_alerts(
    camera_id: str | None = Query(
        default=None,
        description="Filter berdasarkan Camera ID",
    ),
    severity: str | None = Query(
        default=None,
        description="Filter berdasarkan severity",
    ),
):
    collection = get_collection()

    query = {}

    if camera_id:
        query["camera_id"] = camera_id

    if severity:
        query["severity"] = severity

    alerts = list(
        collection.find(
            query,
            {"_id": 0},
        ).sort(
            "timestamp",
            -1,
        )
    )

    return {
        "status": "ok",
        "data": alerts,
    }


@router.post("/", status_code=201)
async def create_alert(alert: AlertCreate):
    collection = get_collection()

    alert_data = alert.model_dump()

    collection.insert_one(alert_data)

    return {
        "status": "ok",
        "message": "Alert created successfully.",
        "data": alert_data,
    }