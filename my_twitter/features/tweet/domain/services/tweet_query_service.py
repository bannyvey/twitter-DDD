from core.services.base_query_service import BaseQueryService
from features.tweet.domain.entities.tweet_query_model import TweetReadModel


class TweetQueryService(BaseQueryService[TweetReadModel]):
    pass
