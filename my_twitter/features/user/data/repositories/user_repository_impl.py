from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from my_twitter.features.user import User
from my_twitter.features.user.domain.entities.user_entity import UserEntity
from my_twitter.features.user.domain.repositories.user_repository import UserRepository


class UserRepositoryImpl(UserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_follow(self, user: UserEntity, id_: int) -> bool:
        res = await self.session.scalars(select(User).where(User.id == user.id).options(selectinload(User.following)))
        current_user = res.first()
        if not current_user:
            return False
        target: User | None = await self.session.get(User, id_)
        if target is None:
            return False
        if target in current_user.following:
            return False  # Уже подписан
        current_user.following.append(target)
        return True

    async def delete_follow(self, user: UserEntity, id_: int) -> bool:
        res = await self.session.scalars(select(User).where(User.id == user.id).options(selectinload(User.following)))
        current_user = res.first()
        if not current_user:
            return False
        target: User | None = await self.session.get(User, id_)
        if target is None:
            return False
        if target not in current_user.following:
            return False  # Уже не был в подписках
        current_user.following.remove(target)
        return True

    async def create(self, entity: UserEntity) -> UserEntity:
        pass

    async def delete(self, entity: UserEntity) -> None:
        pass

    async def find_all(self):
        pass

    async def update(self, entity: UserEntity) -> UserEntity:
        pass
