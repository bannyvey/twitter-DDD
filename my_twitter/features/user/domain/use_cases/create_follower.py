from core.error.user_exception import UserNotFound
from core.use_case.use_case import BaseUseCase
from features.user.domain.entities.user_entity import UserEntity
from features.user.domain.repositories.user_unit_of_work import UserUnitOfWork


class CreateFollowerUseCase(BaseUseCase[UserEntity, int]):
    unit_of_work: UserUnitOfWork

    async def __call__(self, current_user: UserEntity | None = None, id_: int | None = None) -> None:
        raise NotImplementedError


class CreateFollowerUseCaseImpl(CreateFollowerUseCase):
    def __init__(self, unit_of_work: UserUnitOfWork):
        self.unit_of_work = unit_of_work

    async def __call__(self, current_user: UserEntity | None = None, id_: int | None = None) -> None:
        try:

            result = await self.unit_of_work.repository.create_follow(current_user, id_)
            if not result:
                raise UserNotFound("Пользователь не найден или не был в подписках")
        except Exception as e:
            await self.unit_of_work.rollback()
            raise e
        await self.unit_of_work.commit()
