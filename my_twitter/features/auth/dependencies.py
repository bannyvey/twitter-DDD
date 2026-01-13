from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from my_twitter.core.database.postgres.database import get_db
from my_twitter.features.auth.data.repositories.auth_repository_impl import AuthRepositoryImpl
from my_twitter.features.auth.domain.repositories.auth_repository import AuthRepository


def get_auth_repository(
    session: AsyncSession = Depends(get_db)
) -> AuthRepository:
    return AuthRepositoryImpl(session)
