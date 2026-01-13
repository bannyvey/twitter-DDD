from my_twitter.core.error.base_exception import BaseError


class TweetNotFound(BaseError):
    def __init__(self, message="Твит не найден"):
        super().__init__(message, error_type="tweet_not_found")


class PermissionDenied(BaseError):
    def __init__(self, message="You don't have permission to access this resource"):
        super().__init__(message, error_type="No permission")
