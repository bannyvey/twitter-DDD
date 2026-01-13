from fastapi import Depends, HTTPException, status, APIRouter

from my_twitter.features.auth.dependencies import get_auth_repository
from my_twitter.features.auth.domain.entities.auth_schemas import (
    LoginRequest,
    RegisterRequest,
    RefreshTokenRequest,
    TokenResponse
)
from my_twitter.features.auth.domain.repositories.auth_repository import AuthRepository
from my_twitter.features.auth.domain.services.jwt_service import JWTService

# from my_twitter.features.auth.presentation.routes import router

router = APIRouter()


@router.post("/register", response_model=TokenResponse)
async def register(
        request: RegisterRequest,
        auth_repo: AuthRepository = Depends(get_auth_repository)
):
    """
    Регистрация нового пользователя.
    Возвращает access и refresh токены.
    """
    # Проверяем существует ли email
    if await auth_repo.email_exists(request.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Проверяем существует ли nickname
    if await auth_repo.nickname_exists(request.nickname):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nickname already taken"
        )

    # Хэшируем пароль и создаём пользователя
    hashed_password = JWTService.hash_password(request.password)
    user = await auth_repo.create_user(
        email=request.email,
        hashed_password=hashed_password,
        nickname=request.nickname,
        first_name=request.first_name,
        last_name=request.last_name
    )

    # Генерируем токены
    access_token, refresh_token = JWTService.create_tokens(user.id)

    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token
    )
