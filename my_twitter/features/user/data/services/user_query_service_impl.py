from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from my_twitter.features.user import User
from my_twitter.features.user.domain.entities.user_query_model import UserReadModel
from my_twitter.features.user.domain.services.user_query_service import UserQueryService


class UserQueryServiceImpl(UserQueryService):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_about_me(self) -> UserReadModel | None:
        user = await self.session.scalars(select(User).options(
            selectinload(User.followers),
            selectinload(User.following)
        )
        )
        result = user.first()
        if not result:
            return None
        return result.to_read_model()

    async def find_by_id(self, user_id: int) -> UserReadModel | None:
        user = await self.session.scalars(select(User).where(User.id == user_id).options(
            selectinload(User.followers),
            selectinload(User.following)
        )
        )
        result = user.first()
        if not result:
            return None
        return result.to_read_model()

    async def findall(self) -> List[UserReadModel]:
        pass
