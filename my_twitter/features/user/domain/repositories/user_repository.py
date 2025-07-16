from abc import abstractmethod

from core.repositories.base_repository import BaseTweetRepository
from features.user.data.models.user import User
from features.user.domain.entities.user_entity import UserEntity


class UserRepository(BaseTweetRepository[User]):
    @abstractmethod
    async def create_follow(self, user: UserEntity, id_):
        raise NotImplementedError

    @abstractmethod
    async def delete_follow(self, user: UserEntity, id_):
        raise NotImplementedError
