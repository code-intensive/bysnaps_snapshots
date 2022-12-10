from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi_pagination import add_pagination

from snapshots.config.settings import settings
from snapshots.database.config.setup import set_up_database
from snapshots.middlewares.cors_middleware import CORS_MIDDLEWARE_CONFIG
from snapshots.routers.api.snap_router import snaps_router


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: configured fastAPI application.
    """
    app = FastAPI(**settings.APP_SETTINGS)
    app.add_middleware(**CORS_MIDDLEWARE_CONFIG)
    app.include_router(snaps_router, prefix=settings.API_VERSION)

    @app.on_event("startup")
    async def startup() -> None:
        """Sets up needed config on startup event."""
        await set_up_database()

    app.mount("/static", StaticFiles(directory=settings.STATIC_DIR), name="static")

    return add_pagination(app)
