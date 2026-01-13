from sqlalchemy.ext.asyncio import AsyncSession

from my_twitter.features.user.domain.repositories.user_repository import UserRepository
from my_twitter.features.user.domain.repositories.user_unit_of_work import UserUnitOfWork


class UserUnitOfWorkImpl(UserUnitOfWork):
    def __init__(self, session: AsyncSession, repository: UserRepository):
        self.session = session
        self.repository = repository

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()


