from core.error.base_exception import BaseError


class LikeNotFound(BaseError):
    def __init__(self, message='твит найден'):
        super().__init__(message, error_type='like_not_found')
