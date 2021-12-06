from fastapi import FastAPI
from pydantic import main
from .db.session import init_db


def init_orm():
    init_db()


def init_router(app: FastAPI):

    from .controller.diary_controller import router as diary_router
    from .controller.main_page_controller import router as main_page_router

    for router in [diary_router, main_page_router]:
        app.include_router(router)


def create_app() -> FastAPI:
    app = FastAPI()
    init_orm()
    init_router(app)
    return app
