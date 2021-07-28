from typing import Optional
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from db.services_db import service
import databases
from core.settings import settings
from models.services_model import Service, ServiceIn

database = databases.Database(settings.DATABASE_URL)

class CRUDServices():
    async def get_service_by_id(request: Request, id: int) -> Optional[Service]:
        query = service.select().where(service.c.service_id == id)
        if not database.is_connected:
            await database.connect()
        service_fetch = await database.fetch_all(query)
        serialized_service = jsonable_encoder(service_fetch)
        await database.disconnect()
        return serialized_service

    async def post_service(request: Request, obj_in: ServiceIn) -> Optional[Service]:
        if not database.is_connected:
            await database.connect()
        query = service.insert() 
        values = {
            "money_to_raise": obj_in.money_to_raise,
            "time_hrs": obj_in.time_hrs,
            "description": obj_in.description,
        }
        new_service = await database.execute(query=query, values=values)
        await database.disconnect()
        return new_service