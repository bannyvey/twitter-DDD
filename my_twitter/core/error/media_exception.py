from core.error.base_exception import BaseError


class MediaNotFound(BaseError):
    def __init__(self, message="Файл не предоставлен"):
        super().__init__(message, error_type="media_not_found")