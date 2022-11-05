from fastapi import FastAPI

from config.settings import settings
from database.config.setup import set_up_database
from middlewares.cors_middleware import CORS_MIDDLEWARE_CONFIG
from routers.api.snaps import snaps_router

app = FastAPI(**settings.APP_SETTINGS)
app.include_router(snaps_router, prefix=settings.API_VERSION)
app.add_middleware(**CORS_MIDDLEWARE_CONFIG)


@app.on_event("startup")
async def startup():
    await set_up_database()
