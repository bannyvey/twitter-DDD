from abc import ABC, abstractmethod
from typing import Optional

from pydantic import EmailStr

from my_twitter.features.user import User


class AuthRepository(ABC):
    """Абстрактный репозиторий для аутентификации."""
    
    @abstractmethod
    async def get_user_by_email(self, email: EmailStr) -> Optional[User]:
        """Получить пользователя по email."""
        raise NotImplementedError
    
    @abstractmethod
    async def create_user(
        self, 
        email: str, 
        hashed_password: str, 
        nickname: str, 
        first_name: str, 
        last_name: str
    ) -> User:
        """Создать нового пользователя."""
        raise NotImplementedError
    
    @abstractmethod
    async def email_exists(self, email: str) -> bool:
        """Проверить существует ли email."""
        raise NotImplementedError
    
    @abstractmethod
    async def nickname_exists(self, nickname: str) -> bool:
        """Проверить существует ли nickname."""
        raise NotImplementedError
