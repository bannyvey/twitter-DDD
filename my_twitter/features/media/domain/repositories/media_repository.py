from abc import abstractmethod
from typing import Sequence

from core.repositories.base_repository import BaseTweetRepository
from features.media.domain.entities.media_entity import MediaEntity


class MediaRepository(BaseTweetRepository[MediaEntity]):
    @abstractmethod
    async def find_by_id(self, entity_id: int) -> MediaEntity:
        raise NotImplementedError

