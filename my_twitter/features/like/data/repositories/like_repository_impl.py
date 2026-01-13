from sqlalchemy.ext.asyncio import AsyncSession

from my_twitter.features.like  import Like
from my_twitter.features.like import LikeEntity
from my_twitter.features.like.domain.repositories.like_repository import LikeRepository
from my_twitter.features.user.domain.entities.user_entity import UserEntity


class LikeRepositoryImpl(LikeRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, entity: LikeEntity) -> LikeEntity:
        like = Like.from_entity(entity)
        self.session.add(like)
        return like.to_entity()

    async def delete(self, entity: LikeEntity):
        like = await self.session.get(Like, (entity.user_id, entity.tweet_id))
        await self.session.delete(like)

    async def find_by_like_id(self, like_id: int, current_user: UserEntity) -> LikeEntity | None:
        result = await self.session.get(Like, (current_user.id, like_id))
        if result is None:
            return None
        return result.to_entity()

    async def find_all(self):
        pass

    async def update(self, entity: LikeEntity) -> LikeEntity:
        pass
