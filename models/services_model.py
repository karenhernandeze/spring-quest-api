from datetime import date
from typing import Optional
from pydantic import BaseModel

class Service(BaseModel):
    service_id: Optional[int] = None
    money_to_raise: Optional[str] = None
    time_hrs: Optional[int] = None
    description: Optional[str] = None

class ServiceIn(BaseModel):
    money_to_raise: Optional[str] = None
    time_hrs: Optional[int] = None
    description: Optional[str] = None
    class Config:
        schema_extra = {
            "example": {
                "money_to_raise": 123.5,
                "time_hrs": 123,
                "description": "Special Skills",
            }
        }