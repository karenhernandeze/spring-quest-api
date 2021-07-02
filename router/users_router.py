from typing import List
from fastapi import APIRouter, status, Request
from starlette.responses import JSONResponse
from models.users_model import User
from service.users_service import UserService 

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description" : "Not found"}}
)


@router.get("/", status_code=status.HTTP_200_OK, response_description="List all users", response_model=List[User])
async def get_users(request: Request):
    query = await UserService.get_users(request)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"data": query})

@router.get("/{id}", status_code=status.HTTP_200_OK, response_description="User by id", response_model=User)
async def get_user(request: Request, id: int):
    query = await UserService.get_user_by_id(request, id)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"data": query})
