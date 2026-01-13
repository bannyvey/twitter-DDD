from sqlalchemy.ext.asyncio import AsyncSession

from my_twitter.features.tweet.domain.repositories.tweet_repository import TweetRepository
from my_twitter.features.tweet.domain.repositories.tweet_unit_of_work import TweetUnitOfWork


class TweetUnitOfWorkImpl(TweetUnitOfWork):

    def __init__(self, session: AsyncSession, repository: TweetRepository):
        self.session: AsyncSession = session
        self.repository: TweetRepository = repository

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()


