from typing import List
from fastapi import APIRouter, status, Request
from starlette.responses import JSONResponse
from models.categories_model import Categories
from service.categories_router import CategoriesService 

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
    responses={404: {"description" : "Not found"}}
)


@router.get("/", status_code=status.HTTP_200_OK, response_description="List all categories", response_model=List[Categories])
async def get_all_categories(request: Request):
    query = await CategoriesService.get_categories(request)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"data": query})

@router.get("/{id}", status_code=status.HTTP_200_OK, response_description="List categories by id", response_model=Categories)
async def get_categories_by_id(request: Request, id: int):
    query = await CategoriesService.get_categories_id(request, id)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"data": query})
