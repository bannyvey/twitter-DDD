from datetime import datetime

from my_twitter.core.use_case.use_case import BaseUseCase
from my_twitter.features.media.domain.repositories.media_repository import MediaRepository
from my_twitter.features.tweet.domain.entities.tweet_command_model import TweetCreateModel
from my_twitter.features.tweet.domain.entities.tweet_entity import TweetEntity
from my_twitter.features.tweet.domain.repositories.tweet_unit_of_work import TweetUnitOfWork
from my_twitter.features.user.domain.entities.user_entity import UserEntity


class CreateTweetUseCase(BaseUseCase[TweetCreateModel, UserEntity]):
    unit_of_work: TweetUnitOfWork

    async def __call__(self, args: TweetCreateModel | None = None,
                       current_user: UserEntity | None = None) -> TweetEntity:
        raise NotImplementedError()


class CreateTweetUseCaseImpl(CreateTweetUseCase):

    def __init__(self, unit_of_work: TweetUnitOfWork, media_repository: MediaRepository):
        self.unit_of_work = unit_of_work
        self.media_repository = media_repository

    async def __call__(self, data: TweetCreateModel | None = None,
                       current_user: UserEntity | None = None) -> TweetEntity:

        tweet = TweetEntity(
            id_=None,
            message=data.tweet_data,
            created_at=datetime.now(),
            user_id=current_user.id,
        )
        try:
            created_tweet = await self.unit_of_work.repository.create(tweet)
            print(vars(created_tweet))
            if data.tweet_media_ids:  # 6
                for media_id in data.tweet_media_ids:
                    media = await self.media_repository.find_by_id(media_id)
                    print(vars(media))
                    media.tweet_id = created_tweet.id_
                    print(vars(media))
                    await self.media_repository.update(media)
            await self.unit_of_work.commit()
        except Exception as e:
            await self.unit_of_work.rollback()
            raise
        return created_tweet
