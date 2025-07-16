from fastapi import Depends, Header
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from core.database.postgres.database import get_db
from core.error.base_exception import AuthException
from features.media.dependencies import get_media_repository
from features.media.domain.repositories.media_repository import MediaRepository
from features.tweet.data.repositories.tweet_repository_impl import TweetRepositoryImpl
from features.tweet.data.repositories.tweet_unit_of_work_impl import TweetUnitOfWorkImpl
from features.tweet.data.services.tweet_query_service_impl import TweetQueryServiceImpl
from features.tweet.domain.repositories.tweet_repository import TweetRepository
from features.tweet.domain.repositories.tweet_unit_of_work import TweetUnitOfWork
from features.tweet.domain.services.tweet_query_service import TweetQueryService
from features.tweet.domain.use_cases.create_tweet import CreateTweetUseCase, CreateTweetUseCaseImpl
from features.tweet.domain.use_cases.delete_tweet import DeleteTweetUseCase, DeleteTweetUseCaseImpl
from features.tweet.domain.use_cases.get_tweets import GetTweetsUseCase, GetTweetsUseCaseImpl
from features.user.data.models.user import User


def get_tweet_repository(
        session: AsyncSession = Depends(get_db),
) -> TweetRepository:
    return TweetRepositoryImpl(session)


def get_tweet_query_service(
        session: AsyncSession = Depends(get_db)
) -> TweetQueryService:
    return TweetQueryServiceImpl(session)


def get_tweet_unit_of_work(
        session: AsyncSession = Depends(get_db),
        tweet_repository: TweetRepository = Depends(get_tweet_repository)
) -> TweetUnitOfWork:
    return TweetUnitOfWorkImpl(session, tweet_repository)


def get_tweet_use_case(
        service: TweetQueryService = Depends(get_tweet_query_service)
) -> GetTweetsUseCase:
    return GetTweetsUseCaseImpl(service)


def get_delete_tweet_use_case(
        tweet_unit_of_work: TweetUnitOfWork = Depends(get_tweet_unit_of_work)
) -> DeleteTweetUseCase:
    return DeleteTweetUseCaseImpl(tweet_unit_of_work)


def get_create_tweet_use_case(
        tweet_unit_of_work: TweetUnitOfWork = Depends(get_tweet_unit_of_work),
        media_repository: MediaRepository = Depends(get_media_repository)
) -> CreateTweetUseCase:
    return CreateTweetUseCaseImpl(tweet_unit_of_work, media_repository)
