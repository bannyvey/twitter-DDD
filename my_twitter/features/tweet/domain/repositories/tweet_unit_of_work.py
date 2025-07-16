from core.unit_of_work.unit_of_work import AbstractUnitOfWork
from features.tweet.domain.repositories.tweet_repository import TweetRepository


class TweetUnitOfWork(AbstractUnitOfWork[TweetRepository]):
    pass
