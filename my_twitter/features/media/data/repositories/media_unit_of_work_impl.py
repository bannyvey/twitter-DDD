from sqlalchemy.ext.asyncio import AsyncSession

from features.media.domain.repositories.media_repository import MediaRepository
from features.media.domain.repositories.media_unit_of_work import MediaUnitOfWork


class MediaUnitOfWorkImpl(MediaUnitOfWork):
    def __init__(self, session: AsyncSession, repository: MediaRepository):
        self.session = session
        self.repository = repository

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()