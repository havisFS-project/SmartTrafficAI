from datetime import datetime

from pydantic import BaseModel, Field


class PredictionCreate(BaseModel):
    camera_id: str = Field(min_length=1)
    timestamp: datetime
    predicted_speed: float = Field(ge=0)
    predicted_vehicle_count: int = Field(ge=0)
    predicted_density: str = Field(min_length=1)
    forecast_horizon_minutes: int = Field(gt=0)