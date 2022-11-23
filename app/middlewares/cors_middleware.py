from fastapi.middleware.cors import CORSMiddleware

from app.config.settings import settings

CORS_MIDDLEWARE_CONFIG = {
    "allow_methods": ["*"],
    "allow_headers": ["*"],
    "allow_origins": settings.ALLOWED_ORIGINS,
    "allow_credentials": True,
    "middleware_class": CORSMiddleware,
}
