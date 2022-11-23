from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.config.settings import settings
from app.database.config.setup import set_up_database
from app.middlewares.cors_middleware import CORS_MIDDLEWARE_CONFIG
from app.routers.api.snap_router import snaps_router


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI(**settings.APP_SETTINGS)
    app.add_middleware(**CORS_MIDDLEWARE_CONFIG)
    app.include_router(snaps_router, prefix=settings.API_VERSION)

    @app.on_event("startup")
    async def startup() -> None:
        """Sets up needed config on startup event."""
        await set_up_database()

    return add_pagination(app)
