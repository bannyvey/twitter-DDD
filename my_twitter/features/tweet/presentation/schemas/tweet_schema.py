from typing import List

from pydantic import BaseModel, ConfigDict, Field, computed_field


class TweetResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    result: bool = True
    tweet_id: int


