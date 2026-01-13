from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from my_twitter.features.media import Media, MediaEntity
from my_twitter.features.media.domain.repositories.media_repository import MediaRepository


class MediaRepositoryImpl(MediaRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, entity: MediaEntity) -> MediaEntity:
        media = await Media.from_entity(entity)
        self.session.add(media)
        await self.session.flush()
        await self.session.refresh(media)
        return await media.to_entity()

    async def delete(self, entity: MediaEntity) -> None:
        pass

    async def find_all(self) -> Sequence[MediaEntity]:
        pass

    async def find_by_id(self, entity_id: int) -> MediaEntity:
        orm_media = await self.session.scalars(select(Media).where(Media.id == entity_id))
        media = orm_media.first()
        return await media.to_entity()

    async def update(self, entity: MediaEntity) -> MediaEntity:
        media = await self.session.get(Media, entity.id_)
        media.tweet_id = entity.tweet_id
        await self.session.flush()
        await self.session.refresh(media)
        return await media.to_entity()


