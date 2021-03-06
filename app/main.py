from fastapi import FastAPI

from app.api.routes.api import router as api_router
from app.core.config import API_PREFIX, DEBUG, PROJECT_NAME, VERSION
from app.core.events import create_start_app_handler, create_stop_app_handler
from app.db import models
from app.db.database import engine


def get_application() -> FastAPI:
    models.Base.metadata.create_all(bind=engine)
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)

    application.add_event_handler("startup", create_start_app_handler(application))
    application.add_event_handler("shutdown", create_stop_app_handler(application))

    application.include_router(api_router, prefix=API_PREFIX)

    return application


app = get_application()
