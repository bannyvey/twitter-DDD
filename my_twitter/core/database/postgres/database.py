from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from my_twitter.config import settings

DATABASE_URL = f"postgresql+asyncpg://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"

engine = create_async_engine(DATABASE_URL)
local_async_session = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_db():
    async with local_async_session() as session:
        try:
            yield session
        finally:
            await session.close()
