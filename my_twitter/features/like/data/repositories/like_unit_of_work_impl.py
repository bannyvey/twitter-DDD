from sqlalchemy.ext.asyncio import AsyncSession

from features.like.domain.repositories.like_repository import LikeRepository
from features.like.domain.repositories.like_unit_of_work import LikeUnitOfWork


class LikeUnitOfWorkImpl(LikeUnitOfWork):
    def __init__(self, session: AsyncSession, repository: LikeRepository):
        self.session = session
        self.repository = repository

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
