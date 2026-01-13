from abc import abstractmethod

from my_twitter.core.repositories.base_repository import BaseRepository
from my_twitter.features.user import User
from my_twitter.features.user.domain.entities.user_entity import UserEntity


class UserRepository(BaseRepository[User]):
    @abstractmethod
    async def create_follow(self, user: UserEntity, id_):
        raise NotImplementedError

    @abstractmethod
    async def delete_follow(self, user: UserEntity, id_):
        raise NotImplementedError
