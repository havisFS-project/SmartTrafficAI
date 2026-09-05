from datetime import datetime

from pydantic import BaseModel, Field


class AlertCreate(BaseModel):
    camera_id: str = Field(min_length=1)
    alert_type: str = Field(min_length=1)
    severity: str = Field(min_length=1)
    message: str = Field(min_length=1)
    timestamp: datetime