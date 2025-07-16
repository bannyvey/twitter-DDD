from fastapi import Header, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from core.database.postgres.database import get_db
from core.error.base_exception import AuthException
from features.user.data.models.user import User


async def get_current_user(api_key: str = Header(), session: AsyncSession = Depends(get_db)):
    result = await session.scalars(
        select(User).
        where(User.api_key == api_key).
        options(selectinload(User.followers), selectinload(User.following))
    )
    user: User = result.first()
    if not user:
        raise AuthException("Not authenticated")
    return user.to_entity()
