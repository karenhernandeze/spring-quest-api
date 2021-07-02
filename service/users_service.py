from fastapi import Request, HTTPException
from typing import Optional
from crud.user_crud import CRUDUser
from models.users_model import User

class UserService():
    async def get_users(request: Request) -> Optional[User]:
        retrieved_users = await CRUDUser.get_all_users(request)
        return retrieved_users

    async def get_user_by_id(request: Request, id: int) -> Optional[User]:
        retrieved_user = await CRUDUser.get_user_by_id(request, id)
        return retrieved_user


