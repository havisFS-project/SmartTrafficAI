from datetime import datetime

from pydantic import BaseModel, Field


class VehicleDistribution(BaseModel):
    car: int = Field(default=0, ge=0)
    motorcycle: int = Field(default=0, ge=0)
    bus: int = Field(default=0, ge=0)
    truck: int = Field(default=0, ge=0)


class TrafficDataCreate(BaseModel):
    camera_id: str = Field(min_length=1)
    timestamp: datetime
    vehicle_count: int = Field(ge=0)
    average_speed: float = Field(ge=0)
    density: str = Field(min_length=1)
    vehicle_distribution: VehicleDistribution = Field(
        default_factory=VehicleDistribution,
    )