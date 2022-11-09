from config.settings import settings
from fastapi.middleware.cors import CORSMiddleware

CORS_MIDDLEWARE_CONFIG = {
    "allow_methods": ["*"],
    "allow_headers": ["*"],
    "allow_origins": settings.ALLOWED_ORIGINS,
    "allow_credentials": True,
    "middleware_class": CORSMiddleware,
}
