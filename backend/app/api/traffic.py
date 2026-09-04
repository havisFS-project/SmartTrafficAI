from fastapi import APIRouter

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
async def get_traffic_data():
    collection = get_collection()

    traffic_data = list(
        collection.find(
            {},
            {"_id": 0},
        )
    )

    return {
        "status": "ok",
        "data": traffic_data,
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