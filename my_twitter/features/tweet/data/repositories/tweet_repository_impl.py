from abc import ABC
from typing import List

from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from core.error.tweet_exception import TweetNotFound, PermissionDenied
from features.like.data.models.like import Like
from features.tweet.data.models.tweet import Tweet
from features.tweet.domain.entities.tweet_entity import TweetEntity
from features.tweet.domain.repositories.tweet_repository import TweetRepository
from features.user.data.models.user import User
from features.user.domain.entities.user_entity import UserEntity


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
