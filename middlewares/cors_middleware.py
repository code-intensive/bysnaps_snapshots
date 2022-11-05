from fastapi.middleware.cors import CORSMiddleware

origins = ("http://127.0.0.1:3000",)

CORS_MIDDLEWARE_CONFIG = {
    "allow_methods": ["*"],
    "allow_headers": ["*"],
    "allow_origins": origins,
    "allow_credentials": True,
    "middleware_class": CORSMiddleware,
}
