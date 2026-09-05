from datetime import datetime

from fastapi import APIRouter, Query

from app.core.config import settings
from app.db.mongodb import get_client
from app.schemas.traffic import TrafficDataCreate


router = APIRouter(
    prefix="/api/traffic",
    tags=["Traffic"],
)


def get_collection():
    client = get_client()
    database = client[settings.DATABASE_NAME]

    return database["traffic_data"]


@router.get("/")
async def get_traffic_data(
    camera_id: str | None = Query(
        default=None,
        description="Filter berdasarkan Camera ID",
    ),
    start_time: datetime | None = Query(
        default=None,
        description="Waktu awal",
    ),
    end_time: datetime | None = Query(
        default=None,
        description="Waktu akhir",
    ),
):
    collection = get_collection()

    query = {}

    if camera_id:
        query["camera_id"] = camera_id

    if start_time or end_time:
        query["timestamp"] = {}

        if start_time:
            query["timestamp"]["$gte"] = start_time

        if end_time:
            query["timestamp"]["$lte"] = end_time

    traffic_data = list(
        collection.find(
            query,
            {"_id": 0},
        ).sort(
            "timestamp",
            1,
        )
    )

    return {
        "status": "ok",
        "data": traffic_data,
    }

@router.get("/statistics")
async def get_traffic_statistics(
    camera_id: str | None = Query(
        default=None,
        description="Filter berdasarkan Camera ID",
    ),
    start_time: datetime | None = Query(
        default=None,
        description="Waktu awal",
    ),
    end_time: datetime | None = Query(
        default=None,
        description="Waktu akhir",
    ),
):
    collection = get_collection()

    query = {}

    if camera_id:
        query["camera_id"] = camera_id

    if start_time or end_time:
        query["timestamp"] = {}

        if start_time:
            query["timestamp"]["$gte"] = start_time

        if end_time:
            query["timestamp"]["$lte"] = end_time

    records = list(
        collection.find(
            query,
            {"_id": 0},
        )
    )

    total_records = len(records)
    total_vehicles = sum(
        record["vehicle_count"]
        for record in records
    )

    average_speed = (
        sum(record["average_speed"] for record in records)
        / total_records
        if total_records
        else 0
    )

    density = {}

    for record in records:
        level = record["density"]

        density[level] = density.get(level, 0) + 1

    return {
        "status": "ok",
        "camera_id": camera_id,
        "total_records": total_records,
        "total_vehicles": total_vehicles,
        "average_speed": round(average_speed, 2),
        "density": density,
    }

@router.post("/", status_code=201)
async def create_traffic_data(
    traffic: TrafficDataCreate,
):
    collection = get_collection()

    traffic_data = traffic.model_dump()

    collection.insert_one(traffic_data)

    return {
        "status": "ok",
        "message": "Traffic data created successfully.",
        "data": traffic_data,
    }