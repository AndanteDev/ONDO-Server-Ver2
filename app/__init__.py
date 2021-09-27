from fastapi import FastAPI
from app.db.mapper import start_mappers



def init_orm():
    start_mappers()


def create_app() -> FastAPI:
    app = FastAPI()
    init_orm()
    return app