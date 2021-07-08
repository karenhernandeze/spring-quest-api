from datetime import date
from typing import List, Optional
from pydantic import BaseModel

class Project(BaseModel):
    project_id: Optional[int] = None
    userId: Optional[str] = None
    projectName: Optional[str] = None
    projectType: Optional[str] = None
    description: Optional[str] = None
    exepctedStartDate: Optional[date] = None
    exepctedEndDate: Optional[date] = None
    country: Optional[str] = None
    city: Optional[str] = None
    categoryId: Optional[str] = None
    collaboratorsId: Optional[List[int]] = None
    photosId: Optional[str] = None
    phases: Optional[int] = None
    donorsid: Optional[str] = None
    serviceId: Optional[str] = None

class ProjectIn(BaseModel):
    userId: Optional[str] = None
    projectName: Optional[str] = None
    projectType: Optional[str] = None
    description: Optional[str] = None
    exepctedStartDate: Optional[date] = None
    exepctedEndDate: Optional[date] = None
    country: Optional[str] = None
    city: Optional[str] = None
    categoryId: Optional[str] = None
    collaboratorsId: Optional[List[int]] = None
    photosId: Optional[str] = None
    phases: Optional[int] = None
    donorsid: Optional[str] = None
    serviceId: Optional[str] = None
    class Config:
        schema_extra = {
            "example": {
                "userId": "2615283",
                "projectName": "This is My New Project",
                "projectType": "angel",
                "description": "Project Description",
                "exepctedStartDate": "2021-06-20",
                "exepctedEndDate": "2021-08-20",
                "country": "Mexico",
                "city": "Monterrey",
                "categoryId": "1111111",
                "collaboratorsId": [1,2,3],
                "photosId": "1111111",
                "phases": 2,
                "donorsid": "11111111",
                "serviceId": "1111111"
            }
        }

class ProjectId(BaseModel):
    userId: Optional[str] = None
    projectName: Optional[str] = None
    projectType: Optional[str] = None
    description: Optional[str] = None
    exepctedStartDate: date
    exepctedEndDate: date
    country: Optional[str] = None
    city: Optional[str] = None
    categoryId: Optional[str] = None
    collaboratorsId: Optional[List[int]] = None
    photosId: Optional[str] = None
    phases: Optional[int] = None
    donorsid: Optional[str] = None
    serviceId: Optional[str] = None

