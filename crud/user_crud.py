from typing import Optional
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from db.user_db import user
import databases
from core.settings import settings
from models.users_model import User

database = databases.Database(settings.DATABASE_URL)

class CRUDUser():
    async def get_all_users(request: Request) -> Optional[User]:
        query = user.select() #.where(project.c.project_id == 9284806)
        if not database.is_connected:
            await database.connect()
        users = await database.fetch_all(query)
        serialized_users = jsonable_encoder(users)
        await database.disconnect()
        return serialized_users

    async def get_user_by_id(request: Request, id: int) -> Optional[User]:
        query = user.select().where(user.c.user_id == id)
        if not database.is_connected:
            await database.connect()
        user_retrieved = await database.fetch_all(query)
        serialized_user = jsonable_encoder(user_retrieved)
        await database.disconnect()
        return serialized_user