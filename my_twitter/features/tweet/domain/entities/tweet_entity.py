from datetime import datetime


class TweetEntity(object):
    def __init__(
            self,
            id_: int | None,
            message: str,
            created_at: datetime,
            user_id: int
    ):
        self.id_ = id_
        self.message = message
        self.created_at = created_at
        self.user_id = user_id
