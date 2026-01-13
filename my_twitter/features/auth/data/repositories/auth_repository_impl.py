from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from my_twitter.features.auth.domain.repositories.auth_repository import AuthRepository
from my_twitter.features.user import User


class AuthRepositoryImpl(AuthRepository):
    """Реализация репозитория аутентификации."""
    
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get_user_by_email(self, email: str) -> Optional[User]:
        result = await self.session.scalars(
            select(User).where(User.email == email)
        )
        return result.first()
    
    async def create_user(
        self, 
        email: str, 
        hashed_password: str, 
        nickname: str, 
        first_name: str, 
        last_name: str
    ) -> User:
        user = User(
            email=email,
            hashed_password=hashed_password,
            nickname=nickname,
            first_name=first_name,
            last_name=last_name
        )
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
    
    async def email_exists(self, email: str) -> bool:
        result = await self.session.scalars(
            select(User).where(User.email == email)
        )
        return result.first() is not None
    
    async def nickname_exists(self, nickname: str) -> bool:
        result = await self.session.scalars(
            select(User).where(User.nickname == nickname)
        )
        return result.first() is not None
