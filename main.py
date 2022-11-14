from config.settings import settings
from database.config.setup import set_up_database
from fastapi import FastAPI
from middlewares.cors_middleware import CORS_MIDDLEWARE_CONFIG
from routers.api.snap_router import snaps_router

app = FastAPI(**settings.APP_SETTINGS)
app.add_middleware(**CORS_MIDDLEWARE_CONFIG)
app.include_router(snaps_router, prefix=settings.API_VERSION)


@app.on_event("startup")
async def startup() -> None:
    await set_up_database()
