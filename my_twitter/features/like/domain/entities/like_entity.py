class LikeEntity(object):
    def __init__(self, id: int | None, user_id: int, tweet_id: int):
        self.id = id
        self.user_id = user_id
        self.tweet_id = tweet_id

