class BaseError(Exception):
    def __init__(self, message, error_type):
        self.message = message
        self.error_type = error_type


class AuthException(BaseError):
    def __init__(self, message="Ошибка аутентификации"):
        super().__init__(message, "authentication_error")
