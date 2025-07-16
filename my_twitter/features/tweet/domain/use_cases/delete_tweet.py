from core.error.tweet_exception import TweetNotFound, PermissionDenied
from core.use_case.use_case import BaseUseCase
from features.tweet.domain.repositories.tweet_unit_of_work import TweetUnitOfWork
from features.user.domain.entities.user_entity import UserEntity


class DeleteTweetUseCase(BaseUseCase[int, UserEntity]):
    unit_of_work: TweetUnitOfWork

    async def __call__(self, id_: int | None = None, current_user: UserEntity | None = None) -> None:
        raise NotImplementedError()


class DeleteTweetUseCaseImpl(DeleteTweetUseCase):

    def __init__(self, unit_of_work: TweetUnitOfWork):
        self.unit_of_work = unit_of_work

    async def __call__(self, id_: int | None = None, current_user: UserEntity | None = None) -> None:
        tweet = await self.unit_of_work.repository.find_by_tweet_id(id_)
        if not tweet:
            raise TweetNotFound()
        if tweet.user_id != current_user.id:
            raise PermissionDenied()
        try:
            await self.unit_of_work.repository.delete(tweet)
        except Exception as e:
            await self.unit_of_work.rollback()
            raise
        await self.unit_of_work.commit()

