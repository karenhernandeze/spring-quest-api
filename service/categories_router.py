from fastapi import Request, HTTPException
from typing import Optional
from crud.categories_crud import CRUDCategories
from models.categories_model import Categories

class CategoriesService():
    async def get_categories(request: Request) -> Optional[Categories]:
        categories = await CRUDCategories.get_all_categories(request)
        return categories

    async def get_categories_id(request: Request, id: int) -> Optional[Categories]:
        categories = await CRUDCategories.get_categories_by_id(request, id)
        return categories


