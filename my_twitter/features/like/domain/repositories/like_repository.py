from abc import abstractmethod

from core.repositories.base_repository import BaseTweetRepository
from features.like.domain.entities.like_entity import LikeEntity
from features.user.domain.entities.user_entity import UserEntity


class LikeRepository(BaseTweetRepository[LikeEntity]):
    @abstractmethod
    async def find_by_like_id(self, like_id: int, current_user: UserEntity) -> LikeEntity | None:
        raise NotImplementedError
