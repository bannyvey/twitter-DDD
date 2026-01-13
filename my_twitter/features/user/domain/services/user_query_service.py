from abc import abstractmethod

from my_twitter.core.services.base_query_service import BaseQueryService
from my_twitter.features.user.domain.entities.user_query_model import UserReadModel


class UserQueryService(BaseQueryService[UserReadModel]):
    @abstractmethod
    async def get_about_me(self) -> UserReadModel:
        raise NotImplementedError

    @abstractmethod
    async def find_by_id(self, user_id: int) -> UserReadModel:
        raise NotImplementedError
