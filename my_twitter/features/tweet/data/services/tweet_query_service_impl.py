from sqlalchemy import select, Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from features.like.data.models.like import Like
from features.tweet.data.models.tweet import Tweet
from features.tweet.domain.entities.tweet_query_model import TweetReadModel
from features.tweet.domain.services.tweet_query_service import TweetQueryService


class TweetQueryServiceImpl(TweetQueryService):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def findall(self) -> Sequence[TweetReadModel]:
        tweets = await self.session.scalars(select(Tweet).options(
            selectinload(Tweet.author),
            selectinload(Tweet.likes).selectinload(Like.user),
            selectinload(Tweet.medias)
        ))
        result = tweets.all()
        return [await tweet.to_read_model() for tweet in result]
