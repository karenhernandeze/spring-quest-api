from typing import List
from fastapi import APIRouter, status, Request
from starlette.responses import JSONResponse
from models.services_model import Service, ServiceIn
from service.services_service import ServicesService 

router = APIRouter(
    prefix="/services",
    tags=["services"],
    responses={404: {"description" : "Not found"}}
)

@router.get("/", status_code=status.HTTP_200_OK, response_description="List Services By Id", response_model=List[Service])
async def get_service(request: Request, id: int):
    query = await ServicesService.get_services_by_id(request, id)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"data": query})

@router.post("/new/", status_code=status.HTTP_201_CREATED, response_description="Create new service", response_model=Service)
async def create_service(request: Request, service: ServiceIn):
    query = await ServicesService.create_service(request, service)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"data": query})
