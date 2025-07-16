from core.error.base_exception import BaseError


class UserNotFound(BaseError):
    def __init__(self, message='Пользователь не найден'):
        super().__init__(message, error_type="user_not_found")