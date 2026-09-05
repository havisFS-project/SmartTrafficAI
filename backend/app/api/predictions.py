from fastapi import APIRouter, Query

from app.core.config import settings
from app.db.mongodb import get_client
from app.schemas.prediction import PredictionCreate


router = APIRouter(
    prefix="/api/predictions",
    tags=["Predictions"],
)


def get_collection():
    client = get_client()
    database = client[settings.DATABASE_NAME]

    return database["predictions"]


@router.get("/")
async def get_predictions(
    camera_id: str | None = Query(
        default=None,
        description="Filter berdasarkan Camera ID",
    ),
):
    collection = get_collection()

    query = {}

    if camera_id:
        query["camera_id"] = camera_id

    predictions = list(
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
        "data": predictions,
    }


@router.post("/", status_code=201)
async def create_prediction(
    prediction: PredictionCreate,
):
    collection = get_collection()

    prediction_data = prediction.model_dump()

    collection.insert_one(prediction_data)

    return {
        "status": "ok",
        "message": "Prediction created successfully.",
        "data": prediction_data,
    }