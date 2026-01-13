from my_twitter.core.use_case.use_case import BaseUseCase
from my_twitter.features.user.domain.entities.user_entity import UserEntity
from my_twitter.features.user.domain.entities.user_query_model import UserReadModel
from my_twitter.features.user.domain.services.user_query_service import UserQueryService


class UserGetMeUseCase(BaseUseCase[UserReadModel, UserEntity]):
    service: UserQueryService

    async def __call__(self, current_user: UserEntity | None = None) -> UserReadModel:
        raise NotImplementedError


class UserGetMeUseCaseImpl(UserGetMeUseCase):
    def __init__(self, service: UserQueryService):
        self.service = service

    async def __call__(self, current_user: UserEntity | None = None) -> UserReadModel:
        result = await self.service.get_about_me()

        return result
