from typing import List, Optional
from pydantic import BaseModel

class Project(BaseModel):
    project_id: Optional[int] = None
    userId: Optional[str] = None
    projectName: Optional[str] = None
    projectType: Optional[str] = None
    description: Optional[str] = None
    exepctedStartDate: Optional[str] = None
    exepctedEndDate: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    categoryId: Optional[List[int]] = None
    collaboratorsId: Optional[List[int]] = None
    photosId: Optional[List[str]] = None
    phases: Optional[int] = None
    donorsid: Optional[List[int]] = None
    serviceId: Optional[str] = None

class ProjectIn(BaseModel):
    userId: Optional[str] = None
    projectName: Optional[str] = None
    projectType: Optional[str] = None
    description: Optional[str] = None
    exepctedStartDate: Optional[str] = None
    exepctedEndDate: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    categoryId: Optional[List[int]] = None
    collaboratorsId: Optional[List[int]] = None
    photosId: Optional[List[str]] = None
    phases: Optional[int] = None
    donorsid: Optional[List[int]] = None
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
                "categoryId": [1,2,3],
                "collaboratorsId": [1,2,3],
                "photosId": ["1","2","3"],
                "phases": 2,
                "donorsid": [1,2,3],
                "serviceId": "1111111"
            }
        }

class ProjectId(BaseModel):
    userId: Optional[str] = None
    projectName: Optional[str] = None
    projectType: Optional[str] = None
    description: Optional[str] = None
    exepctedStartDate: Optional[str] = None
    exepctedEndDate: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    categoryId: Optional[List[int]] = None
    collaboratorsId: Optional[List[int]] = None
    photosId: Optional[List[str]] = None
    phases: Optional[int] = None
    donorsid: Optional[List[int]] = None
    serviceId: Optional[str] = None

