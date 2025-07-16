from abc import abstractmethod

from core.repositories.base_repository import BaseTweetRepository

from features.tweet.domain.entities.tweet_entity import TweetEntity
from features.user.domain.entities.user_entity import UserEntity


class TweetRepository(BaseTweetRepository[TweetEntity]):
    @abstractmethod
    async def find_by_tweet_id(self, tweet_id: int) -> TweetEntity:
        raise NotImplementedError
