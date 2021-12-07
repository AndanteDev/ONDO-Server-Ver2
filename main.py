import uvicorn

from app.config import CONFIG
from app import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=CONFIG.WEB_SERVER_HOST,
        port=CONFIG.WEB_SERVER_PORT,
        reload=CONFIG.PROJ_RELOAD,
        workers=1,
    )
