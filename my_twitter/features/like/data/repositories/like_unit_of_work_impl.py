from sqlalchemy.ext.asyncio import AsyncSession

from my_twitter.features.like.data.repositories.like_repository_impl import LikeRepositoryImpl
from my_twitter.features.like.domain.repositories.like_repository import LikeRepository
from my_twitter.features.like.domain.repositories.like_unit_of_work import LikeUnitOfWork


class LikeUnitOfWorkImpl(LikeUnitOfWork):
    def __init__(self, session: AsyncSession, repository: LikeRepositoryImpl):
        self.session = session
        self.repository = repository

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
