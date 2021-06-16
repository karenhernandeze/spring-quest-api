from typing import List
from fastapi import APIRouter, status, Request
from starlette.responses import JSONResponse
from models.projects_model import Project
from models.projects_model import ProjectIn
from service.projects_service import ProjectService 

router = APIRouter(
    prefix="/projects",
    tags=["projects"],
    responses={404: {"description" : "Not found"}}
)


@router.get("/", status_code=status.HTTP_200_OK, response_description="List all projects", response_model=List[Project])
async def get_projects(request: Request):
    query = await ProjectService.get_projects(request)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"data": query})

@router.post("/new/", status_code=status.HTTP_201_CREATED, response_description="Create new project", response_model=Project)
async def create_project(request: Request, project: ProjectIn):
    query = await ProjectService.create_project(request, project)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"data": query})
