from typing import List, Sequence

from my_twitter.core.use_case.use_case import BaseUseCase

from my_twitter.features.tweet.domain.entities.tweet_query_model import TweetReadModel
from my_twitter.features.tweet.domain.services.tweet_query_service import TweetQueryService
from my_twitter.features.user.domain.entities.user_entity import UserEntity


class GetTweetsUseCase(BaseUseCase[UserEntity, Sequence[TweetReadModel]]):
    service: TweetQueryService

    async def __call__(self, current_user: UserEntity | None = None, args: None = None) -> Sequence[TweetReadModel]:
        raise NotImplementedError()


class GetTweetsUseCaseImpl(GetTweetsUseCase):
    def __init__(self, service: TweetQueryService):
        self.service: TweetQueryService = service

    async def __call__(self, current_user: None = None, args: None = None) -> Sequence[TweetReadModel]:
        tweets = await self.service.findall()

        return tweets
