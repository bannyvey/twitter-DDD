from abc import abstractmethod

from my_twitter.core.repositories.base_repository import BaseRepository
from my_twitter.features.like.domain.entities.like_entity import LikeEntity
from my_twitter.features.user.domain.entities.user_entity import UserEntity


class LikeRepository(BaseRepository[LikeEntity]):
    @abstractmethod
    async def find_by_like_id(self, like_id: int, current_user: UserEntity) -> LikeEntity | None:
        raise NotImplementedError
