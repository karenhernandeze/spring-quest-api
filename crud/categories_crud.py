from typing import Optional
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from db.categories_db import categories
import databases
from core.settings import settings
from models.categories_model import Categories

database = databases.Database(settings.DATABASE_URL)

class CRUDCategories():
    async def get_all_categories(request: Request) -> Optional[Categories]:
        query = categories.select() #.where(project.c.project_id == 9284806)
        if not database.is_connected:
            await database.connect()
        categories_retrieved = await database.fetch_all(query)
        serialized_categories = jsonable_encoder(categories_retrieved)
        await database.disconnect()
        return serialized_categories

    async def get_categories_by_id(request: Request, id: int) -> Optional[Categories]:
        query = categories.select().where(categories.c.id == id)
        if not database.is_connected:
            await database.connect()
        categories_retrieved = await database.fetch_all(query)
        serialized_categories = jsonable_encoder(categories_retrieved)
        await database.disconnect()
        return serialized_categories