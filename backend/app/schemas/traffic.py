from datetime import datetime

from pydantic import BaseModel, Field


class TrafficDataCreate(BaseModel):
    camera_id: str = Field(min_length=1)
    timestamp: datetime
    vehicle_count: int = Field(ge=0)
    average_speed: float = Field(ge=0)
    density: str = Field(min_length=1)