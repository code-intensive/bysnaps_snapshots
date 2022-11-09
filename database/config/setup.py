from config.settings import settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

async_engine = create_async_engine(
    settings.db_url,
    future=True,
    echo=settings.db_echo,
)
async_session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)
Model = declarative_base()


async def set_up_database() -> None:
    async with async_engine.begin() as conn:
        # await conn.run_sync(Model.metadata.drop_all)
        await conn.run_sync(Model.metadata.create_all)
