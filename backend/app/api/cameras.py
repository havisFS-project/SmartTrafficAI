from fastapi import APIRouter, HTTPException

from app.db.mongodb import get_client
from app.core.config import settings
from app.schemas.camera import CameraCreate, CameraUpdate


router = APIRouter(
    prefix="/api/cameras",
    tags=["Cameras"],
)

def get_collection():
    client = get_client()
    database = client[settings.DATABASE_NAME]

    return database["cameras"]

@router.get("/")
async def get_cameras():
    collection = get_collection()

    cameras = list(
        collection.find(
            {},
            {"_id": 0},
        )
    )

    return {
        "status": "ok",
        "data": cameras,
    }


@router.get("/{camera_id}")
async def get_camera(camera_id: str):
    collection = get_collection()

    camera = collection.find_one(
        {"camera_id": camera_id},
        {"_id": 0},
    )

    if not camera:
        raise HTTPException(
            status_code=404,
            detail="Camera not found.",
        )

    return {
        "status": "ok",
        "data": camera,
    }


@router.post("/", status_code=201)
async def create_camera(camera: CameraCreate):
    collection = get_collection()

    existing_camera = collection.find_one(
        {"camera_id": camera.camera_id}
    )

    if existing_camera:
        raise HTTPException(
            status_code=409,
            detail="Camera ID already exists.",
        )

    camera_data = camera.model_dump()

    collection.insert_one(camera_data)

    return {
        "status": "ok",
        "message": "Camera created successfully.",
        "data": camera_data,
    }


@router.put("/{camera_id}")
async def update_camera(
    camera_id: str,
    camera: CameraUpdate,
):
    collection = get_collection()

    existing_camera = collection.find_one(
        {"camera_id": camera_id}
    )

    if not existing_camera:
        raise HTTPException(
            status_code=404,
            detail="Camera not found.",
        )

    camera_data = camera.model_dump()

    collection.update_one(
        {"camera_id": camera_id},
        {
            "$set": camera_data,
        },
    )

    updated_camera = collection.find_one(
        {"camera_id": camera_id},
        {"_id": 0},
    )

    return {
        "status": "ok",
        "message": "Camera updated successfully.",
        "data": updated_camera,
    }


@router.delete("/{camera_id}")
async def delete_camera(camera_id: str):
    collection = get_collection()

    existing_camera = collection.find_one(
        {"camera_id": camera_id}
    )

    if not existing_camera:
        raise HTTPException(
            status_code=404,
            detail="Camera not found.",
        )

    collection.delete_one(
        {"camera_id": camera_id}
    )

    return {
        "status": "ok",
        "message": "Camera deleted successfully.",
        "camera_id": camera_id,
    }