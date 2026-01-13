from my_twitter.core.services.base_query_service import BaseQueryService
from my_twitter.features.tweet.domain.entities.tweet_query_model import TweetReadModel


class TweetQueryService(BaseQueryService[TweetReadModel]):
    pass
