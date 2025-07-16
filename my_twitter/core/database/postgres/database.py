from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import settings

from features.tweet.data.models.tweet import Tweet
from features.like.data.models.like import Like
from features.user.data.models.user import User
from features.media.data.models.media import Media

DATABASE_URL = f"postgresql+asyncpg://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"

engine = create_async_engine(DATABASE_URL)
local_async_session = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_db():
    async with local_async_session() as session:
        try:
            yield session
        finally:
            await session.close()
