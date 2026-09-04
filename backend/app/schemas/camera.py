from pydantic import BaseModel, Field


class CameraCreate(BaseModel):
    camera_id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    location: str = Field(min_length=1)
    status: str = Field(default="Live")
    fps: int = Field(default=0, ge=0)

class CameraUpdate(BaseModel):
    name: str = Field(min_length=1)
    location: str = Field(min_length=1)
    status: str = Field(default="Live")
    fps: int = Field(default=0, ge=0)