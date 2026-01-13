from my_twitter.core.use_case.use_case import BaseUseCase
from my_twitter.features.like.data.repositories.like_unit_of_work_impl import LikeUnitOfWorkImpl
from my_twitter.features.like.domain.entities.like_entity import LikeEntity
from my_twitter.features.like.domain.repositories.like_unit_of_work import LikeUnitOfWork
from my_twitter.features.user.domain.entities.user_entity import UserEntity

class CreateLikeUseCase(BaseUseCase[int, LikeEntity]):
    unit_of_work: LikeUnitOfWork

    async def __call__(self, id_: int | None = None, current_user: UserEntity | None = None) -> LikeEntity:
        raise NotImplementedError


class CreateLikeUseCaseImpl(CreateLikeUseCase):

    def __init__(self, unit_of_work: LikeUnitOfWorkImpl):
        self.unit_of_work = unit_of_work

    async def __call__(self, id_: int | None = None, current_user: UserEntity | None = None) -> LikeEntity:
        like = LikeEntity(
            id=None,
            user_id=current_user.id,
            tweet_id=id_
        )
        try:
            created_like = await self.unit_of_work.repository.create(like)
        except Exception:
            await self.unit_of_work.rollback()
            raise
        await self.unit_of_work.commit()
        return created_like
