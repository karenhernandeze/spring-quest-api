from logging import error
from typing import Optional
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from models.projects_model import Project
from db.project_db import project
import databases
from core.settings import settings
from models.projects_model import ProjectIn

database = databases.Database(settings.DATABASE_URL)

class CRUDProject():
    async def get_all_projects(request: Request) -> Optional[Project]:
        query = project.select() #.where(project.c.project_id == 9284806)
        if not database.is_connected:
            await database.connect()
        projects = await database.fetch_all(query)
        serialized_hours = jsonable_encoder(projects)
        await database.disconnect()
        return serialized_hours

    async def get_all_projects_by_user_id(request: Request, user_id: str) -> Optional[Project]:
        query = project.select().where(project.c.userid == user_id)
        if not database.is_connected:
            await database.connect()
        projects = await database.fetch_all(query)
        serialized_projects = jsonable_encoder(projects)
        await database.disconnect()
        return serialized_projects

    async def post_project(request: Request, obj_in: ProjectIn) -> Optional[Project]:
        try:
            print(1)
            if not database.is_connected:
                await database.connect()
            print(2)
            
            query = project.insert() 
            print(3)

            values = {
                "userid": obj_in.userId,
                "projectname": obj_in.projectName,
                "projecttype": obj_in.projectType,
                "description": obj_in.description,
                "exepctedstartdate": obj_in.exepctedStartDate,
                "exepctedenddate": obj_in.exepctedEndDate,
                "country": obj_in.country,
                "city": obj_in.city,
                "categoryid": obj_in.categoryId,
                "collaboratorsid": obj_in.collaboratorsId, 
                "photosid": obj_in.photosId,
                "phases": obj_in.phases,
                "donorsid": obj_in.donorsid,
                "serviceid": obj_in.serviceId
            }
            print(4.1)

            new_project = await database.execute(query=query, values=values)
            print(4)
            
            await database.disconnect()
            print(5)

            return new_project
        except error:
            print('error at crud')