from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from my_twitter.core.database.postgres.database import get_db
from my_twitter.core.error.base_exception import AuthException
from my_twitter.features.auth.domain.services.jwt_service import JWTService
from my_twitter.features.user import User


# Схема для получения Bearer токена из заголовка Authorization
security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    session: AsyncSession = Depends(get_db)
):
    """
    Получает текущего пользователя из JWT токена.
    Используется как зависимость для защищённых эндпоинтов.
    """
    token = credentials.credentials
    
    # Декодируем токен
    payload = JWTService.decode_token(token)
    
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    # Проверяем тип токена
    if payload.get("type") != "access":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token type",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    user_id = int(payload.get("sub"))
    
    # Получаем пользователя из БД
    result = await session.scalars(
        select(User).
        where(User.id == user_id).
        options(selectinload(User.followers), selectinload(User.following))
    )
    user: User = result.first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    return user.to_entity()

