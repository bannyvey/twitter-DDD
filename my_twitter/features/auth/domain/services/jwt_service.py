from datetime import datetime, timedelta, timezone
from typing import Optional

import bcrypt
from jose import jwt, JWTError

from my_twitter.config import settings


class JWTService:
    """Сервис для работы с JWT токенами и хэшированием паролей."""
    
    @staticmethod
    def hash_password(password: str) -> str:
        """Хэширует пароль с использованием bcrypt."""
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password_bytes, salt).decode('utf-8')
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Проверяет соответствие пароля хэшу."""
        password_bytes = plain_password.encode('utf-8')
        hashed_bytes = hashed_password.encode('utf-8')
        return bcrypt.checkpw(password_bytes, hashed_bytes)
    
    @staticmethod
    def create_access_token(user_id: int) -> str:
        """Создаёт access token с коротким сроком жизни."""
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.access_token_expire_minutes
        )
        payload = {
            "sub": str(user_id),
            "exp": expire,
            "type": "access"
        }
        return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
    
    @staticmethod
    def create_refresh_token(user_id: int) -> str:
        """Создаёт refresh token с длинным сроком жизни."""
        expire = datetime.now(timezone.utc) + timedelta(
            days=settings.refresh_token_expire_days
        )
        payload = {
            "sub": str(user_id),
            "exp": expire,
            "type": "refresh"
        }
        return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
    
    @staticmethod
    def decode_token(token: str) -> Optional[dict]:
        """Декодирует и валидирует токен. Возвращает None если токен невалидный."""
        try:
            payload = jwt.decode(
                token, 
                settings.jwt_secret_key, 
                algorithms=[settings.jwt_algorithm]
            )
            return payload
        except JWTError:
            return None
    
    @staticmethod
    def create_tokens(user_id: int) -> tuple[str, str]:
        """Создаёт пару токенов (access + refresh)."""
        access_token = JWTService.create_access_token(user_id)
        refresh_token = JWTService.create_refresh_token(user_id)
        return access_token, refresh_token
