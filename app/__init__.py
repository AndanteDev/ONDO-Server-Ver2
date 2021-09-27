from fastapi import FastAPI
from app.db.session import init_db



def init_orm():
    init_db()


def create_app() -> FastAPI:
    app = FastAPI()
    init_orm()
    return app