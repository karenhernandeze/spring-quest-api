from fastapi import Request, HTTPException
from typing import Optional
from crud.services_crud import CRUDServices
from models.services_model import Service, ServiceIn

class ServicesService():
    async def get_services_by_id(request: Request, id: int) -> Optional[Service]:
        retrieved_service = await CRUDServices.get_service_by_id(request, id)
        return retrieved_service

    async def create_service(request: Request, obj_in: ServiceIn) -> Optional[ServiceIn]:
        new_service = await CRUDServices.post_service(request, obj_in)
        if not new_service:
                raise HTTPException(
                status_code=404, 
                detail="Could not be created"
            )
        return new_service


