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

    async def post_project(request: Request, obj_in: ProjectIn) -> Optional[Project]:
        if not database.is_connected:
            await database.connect()
        query = project.insert() 
        values = {
            "userid": obj_in.userId,
            "projectname": obj_in.projectName,
            "projecttype": obj_in.projectType,
            "exepctedstartdate": obj_in.exepctedStartDate,
            "exepctedenddate": obj_in.exepctedEndDate,
            "country": obj_in.country,
            "city": obj_in.city,
            "categoryid": obj_in.categoryId,
            "collaboratorsid": obj_in.collaboratorsId, 
            "photosid": obj_in.photosId,
            "phases": obj_in.phases,
            "currentphase": obj_in.currentPhase,
            "serviceid": obj_in.serviceId
        }
        new_project = await database.execute(query=query, values=values)
        await database.disconnect()
        return new_project