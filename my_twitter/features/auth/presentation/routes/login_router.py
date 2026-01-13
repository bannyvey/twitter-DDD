from fastapi import Depends, HTTPException, status
from fastapi import  APIRouter

from my_twitter.features.auth.dependencies import get_auth_repository
from my_twitter.features.auth.domain.entities.auth_schemas import (
    LoginRequest,
    RegisterRequest,
    RefreshTokenRequest,
    TokenResponse
)
from my_twitter.features.auth.domain.repositories.auth_repository import AuthRepository
from my_twitter.features.auth.domain.services.jwt_service import JWTService

router = APIRouter()


@router.post("/login", response_model=TokenResponse)
async def login(
        request: LoginRequest,
        auth_repo: AuthRepository = Depends(get_auth_repository)
):
    """
    Вход пользователя.
    Возвращает access и refresh токены.
    """
    # Ищем пользователя по email
    user = await auth_repo.get_user_by_email(request.email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # Проверяем пароль
    if not JWTService.verify_password(request.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # Генерируем токены
    access_token, refresh_token = JWTService.create_tokens(user.id)

    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token
    )


@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(
    request: RefreshTokenRequest,
    auth_repo: AuthRepository = Depends(get_auth_repository)
):
    """
    Обновление access токена с помощью refresh токена.
    """
    # Декодируем refresh token
    payload = JWTService.decode_token(request.refresh_token)

    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token"
        )

    # Проверяем тип токена
    if payload.get("type") != "refresh":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token type"
        )

    user_id = int(payload.get("sub"))

    # Генерируем новые токены
    access_token, new_refresh_token = JWTService.create_tokens(user_id)

    return TokenResponse(
        access_token=access_token,
        refresh_token=new_refresh_token
    )