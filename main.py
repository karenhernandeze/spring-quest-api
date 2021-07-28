from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
import databases
import sqlalchemy
from router import projects_router, services_router, users_router, categories_router

# CONNECTING TO DB 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))
DATABASE_URL= os.environ["DATABASE_URL"]
database = databases.Database(DATABASE_URL)


engine = sqlalchemy.create_engine(
    DATABASE_URL
) 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def hello():
    return {"message": "Hello this is the base project."}

app.include_router(router=projects_router.router) 
app.include_router(router=users_router.router) 
app.include_router(router=categories_router.router) 
app.include_router(router=services_router.router) 