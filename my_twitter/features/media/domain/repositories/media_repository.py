from abc import abstractmethod
from typing import Sequence

from my_twitter.core.repositories.base_repository import BaseRepository
from my_twitter.features.media.domain.entities.media_entity import MediaEntity


class MediaRepository(BaseRepository[MediaEntity]):
    @abstractmethod
    async def find_by_id(self, entity_id: int) -> MediaEntity:
        raise NotImplementedError

