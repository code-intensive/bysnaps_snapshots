import enum
from os import getenv
from pathlib import Path
from tempfile import gettempdir

import cloudinary
from dotenv import load_dotenv
from pydantic import BaseSettings
from yarl import URL


class LogLevel(str, enum.Enum):  # noqa: WPS600
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    API_VERSION = "/v1"
    TEMP_DIR = Path(gettempdir())
    PROJECT_ROOT = Path(__file__).parent.parent
    DOT_ENV_PATH = PROJECT_ROOT.joinpath("config/env/development/.env")

    load_dotenv(dotenv_path=DOT_ENV_PATH)

    PROJECT_DESCRIPTION = (
        "The core snap processing service for the buysnaps microservices project"
    )

    APP_SETTINGS = {
        "version": "0.1.0",
        "title": "Buysnaps | Snaps [v1]",
        "debug": getenv("DEBUG", False),
        "description": PROJECT_DESCRIPTION,
    }

    DATABASE_URL = "sqlite+aiosqlite:///./snap_shot.db"

    host: str = "127.0.0.1"
    port: int = 8000
    # quantity of workers for uvicorn
    workers_count: int = 1
    # Enable uvicorn reloading
    reload: bool = False

    # Current environment
    environment: str = "dev"

    log_level: LogLevel = LogLevel.INFO

    # Variables for the database

    db_scheme = str(getenv("DB_SCHEME"))
    db_host = str(getenv("DB_HOST"))
    db_port = int(getenv("DB_PORT", 0))
    db_user: str | None = getenv("DB_USER")
    db_pass: str | None = getenv("DB_PASS")
    db_base = str(getenv("DB_BASE"))
    db_echo = bool(getenv("DB_ECHO"))

    # Variables for Redis
    redis_host: str = "snapshots-redis"
    redis_port: int = 6379
    redis_user: str | None = None
    redis_pass: str | None = None
    redis_base: int | None = None

    # Variables for RabbitMQ
    rabbit_host: str = "snapshots-rmq"
    rabbit_port: int = 5672
    rabbit_user: str = "guest"
    rabbit_pass: str = "guest"
    rabbit_vhost: str = "/"

    rabbit_pool_size: int = 2
    rabbit_channel_pool_size: int = 10

    # This variable is used to define
    # multiproc_dir. It's required for [uvi|guni]corn projects.

    prometheus_dir: Path = TEMP_DIR / "prom"

    CLOUDINARY_SETTINGS = {
        "api_key": getenv("API_KEY"),
        "cloud_name": getenv("CLOUD_NAME"),
        "api_secret": getenv("API_SECRET"),
    }

    CLOUDINARY_SNAP_UPLOAD_FOLDER: str = "buysnaps/snap-shots/"

    @property
    def db_url(self) -> URL:
        """
        Assemble database URL from settings.

        :return: database URL.
        """
        return URL.build(
            scheme=self.db_scheme,
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            password=self.db_pass,
            path=f"/{self.db_base}",
        )

    @property
    def redis_url(self) -> URL:
        """
        Assemble REDIS URL from settings.

        :return: redis URL.
        """
        path = ""
        if self.redis_base is not None:
            path = f"/{self.redis_base}"
        return URL.build(
            scheme="redis",
            host=self.redis_host,
            port=self.redis_port,
            user=self.redis_user,
            password=self.redis_pass,
            path=path,
        )

    @property
    def rabbit_url(self) -> URL:
        """
        Assemble RabbitMQ URL from settings.

        :return: rabbit URL.
        """
        return URL.build(
            scheme="amqp",
            host=self.rabbit_host,
            port=self.rabbit_port,
            user=self.rabbit_user,
            password=self.rabbit_pass,
            path=self.rabbit_vhost,
        )


settings = Settings()
cloudinary.config(**settings.CLOUDINARY_SETTINGS)
