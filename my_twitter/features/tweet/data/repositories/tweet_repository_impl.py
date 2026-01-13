from sqlalchemy.ext.asyncio import AsyncSession

from my_twitter.features.tweet import Tweet
from my_twitter.features.tweet.domain.entities.tweet_entity import TweetEntity
from my_twitter.features.tweet.domain.repositories.tweet_repository import TweetRepository


class TweetRepositoryImpl(TweetRepository):
    def __init__(self, session):
        self.session: AsyncSession = session

    async def create(self, entity: TweetEntity) -> TweetEntity:
        tweet = await Tweet.from_entity(entity)
        self.session.add(tweet)
        await self.session.flush()
        await self.session.refresh(tweet)
        return tweet.to_entity()

    async def find_by_tweet_id(self, tweet_id: int) -> TweetEntity | None:
        tweet = await self.session.get(Tweet, tweet_id)
        if tweet is None:
            return None
        return tweet.to_entity()

    async def delete(self, entity: TweetEntity) -> None:
        tweet = await self.session.get(Tweet, entity.id_)
        await self.session.delete(tweet)

    async def find_all(self):
        pass

    async def update(self, entity: TweetEntity) -> TweetEntity:
        pass
