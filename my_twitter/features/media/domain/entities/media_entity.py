class MediaEntity(object):
    def __init__(self, id_: int | None, path: str, tweet_id: int | None = None):
        self.id_ = id_
        self.path = path
        self.tweet_id = tweet_id


