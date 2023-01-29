from enum import Enum
from os import getenv
from pathlib import Path
from tempfile import gettempdir

import cloudinary
from dotenv import load_dotenv
from yarl import URL

load_dotenv()


class LogLevel(str, Enum):  # noqa: WPS600
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings:
    """
    Application settings.

    These parameters can be configured

    with environment variables.
    """

    APP_ROOT = Path(__file__).parent.parent

    API_VERSION = "/api/v1"
    TEMP_DIR = Path(gettempdir())
    DEBUG = getenv("DEBUG", False)
    RESOURCES_DIR = APP_ROOT.joinpath("resources").as_posix()

    PROJECT_DESCRIPTION = (
        "The core snap processing service for the bysnaps microservices project."
    )

    APP_SETTINGS = {
        "version": "0.1.0",
        "title": "Bysnaps | Snapshots [v1]",
        "debug": DEBUG,
        "description": PROJECT_DESCRIPTION,
        "docs_url": API_VERSION + "/docs",
        "redoc_url": API_VERSION + "/redocs",
    }

    host: str | None = getenv("HOST")
    port: str | None = getenv("PORT")
    # quantity of workers for uvicorn
    workers_count: int = 1
    # Enable uvicorn reloading
    reload: str | bool = getenv("RELOAD_SNAPSHOTS", False)
    use_factory: str | bool = getenv("USE_FACTORY", False)

    # Current environment
    environment: str = getenv("ENVIRON", "dev")

    log_level: LogLevel = LogLevel.INFO

    # Variables for the database

    db_scheme = str(getenv("DB_SCHEME"))
    db_host = str(getenv("DB_HOST"))
    db_port = int(getenv("DB_PORT", 0))
    db_user: str | None = getenv("DB_USER")
    db_pass: str | None = getenv("DB_PASSWORD")
    db_name = str(getenv("DB_NAME"))
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
        "api_key": getenv("CLOUD_API_KEY"),
        "cloud_name": getenv("CLOUD_NAME"),
        "api_secret": getenv("CLOUD_API_SECRET"),
    }

    CLOUD_SNAP_UPLOAD_FOLDER: str | None = getenv("SNAP_UPLOAD_FOLDER")

    ALLOWED_ORIGINS = ("http://127.0.0.1:3000",)

    @property
    def db_url(self) -> str:
        """
        Assemble database URL from settings.

        :return: database URL.
        """
        return str(
            URL.build(
                scheme=self.db_scheme,
                host=self.db_host,
                port=self.db_port,
                user=self.db_user,
                password=self.db_pass,
                path=self.db_name,
            ),
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
