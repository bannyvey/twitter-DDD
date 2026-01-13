from my_twitter.core.error.user_exception import UserNotFound
from my_twitter.core.use_case.use_case import BaseUseCase
from my_twitter.features.user.domain.entities.user_query_model import UserReadModel
from my_twitter.features.user.domain.services.user_query_service import UserQueryService


class FindByIdUserUseCase(BaseUseCase[int, UserReadModel]):
    service: UserQueryService

    async def __call__(self, id_: int | None = None) -> UserReadModel:
        raise NotImplementedError


class FindByIdUserUseCaseImpl(FindByIdUserUseCase):
    def __init__(self, service: UserQueryService):
        self.service = service

    async def __call__(self, id_: int | None = None) -> UserReadModel:
        result = await self.service.find_by_id(id_)
        if result is None:
            raise UserNotFound
        return result
