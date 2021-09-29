from logging import error
from fastapi import Request, HTTPException
from typing import Optional
from crud.project_crud import CRUDProject
from models.projects_model import Project
from models.projects_model import ProjectIn

class ProjectService():
    async def get_projects(request: Request) -> Optional[Project]:
        try:
            retrieved_projects = await CRUDProject.get_all_projects(request)
            return retrieved_projects
        except error: 
            return "too many connections for role qpyosdmwfbbiyc"

    async def get_all_projects_by_user(request: Request, user_id: str) -> Optional[Project]:
        retrieved_projects = await CRUDProject.get_all_projects_by_user_id(request, user_id)
        return retrieved_projects

    async def create_project(request: Request, obj_in: ProjectIn) -> Optional[Project]:
        try:
            print(obj_in)
            new_project = await CRUDProject.post_project(request, obj_in)
            if not new_project:
                raise HTTPException(
                status_code=404, 
                detail="Could not be created"
            )
            print(new_project)
            return new_project
        except:
            print('error at service')
        


