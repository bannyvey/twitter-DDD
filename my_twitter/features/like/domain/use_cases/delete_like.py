from my_twitter.core.error.like_exception import LikeNotFound
from my_twitter.core.use_case.use_case import BaseUseCase
from my_twitter.features.like.domain.entities.like_entity import LikeEntity
from my_twitter.features.like.domain.repositories.like_unit_of_work import LikeUnitOfWork
from my_twitter.features.user.domain.entities.user_entity import UserEntity


class DeleteLikeUseCase(BaseUseCase[int, LikeEntity]):
    unit_of_work: LikeUnitOfWork

    async def __call__(self, id_: int | None = None, current_user: UserEntity | None = None) -> LikeEntity:
        raise NotImplementedError


class DeleteLikeUseCaseImpl(DeleteLikeUseCase):
    def __init__(self, unit_of_work: LikeUnitOfWork):
        self.unit_of_work = unit_of_work

    async def __call__(self, id_: int | None = None, current_user: UserEntity | None = None) -> LikeEntity:
        like = await self.unit_of_work.repository.find_by_like_id(id_, current_user)
        if not like:
            raise LikeNotFound
        try:
            await self.unit_of_work.repository.delete(like)
        except Exception as e:
            raise e
        await self.unit_of_work.commit()
