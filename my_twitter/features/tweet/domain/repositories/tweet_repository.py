from abc import abstractmethod

from my_twitter.core.repositories.base_repository import BaseRepository

from my_twitter.features.tweet.domain.entities.tweet_entity import TweetEntity
from my_twitter.features.user.domain.entities.user_entity import UserEntity


class TweetRepository(BaseRepository[TweetEntity]):
    @abstractmethod
    async def find_by_tweet_id(self, tweet_id: int) -> TweetEntity:
        raise NotImplementedError
