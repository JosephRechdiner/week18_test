from typing import Literal
from pydantic import BaseModel, Field

class Alert(BaseModel):
    border: Literal["egypt", "lebanon", "gaza", "syria", "jordan"]
    zone: str
    timestamp: str
    people_count: int
    weapons_count: int
    vehicle_type: Literal["motorcycle", "jeep", "truck", "car", "none"]
    distance_from_fence_m: int
    visibility_quality: float | int = Field(gt=-1, ls=100)
