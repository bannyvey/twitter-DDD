from typing import Optional, List

from pydantic import BaseModel, Field


class TweetCreateModel(BaseModel):
    tweet_data: str
    tweet_media_ids: Optional[List[int]] = Field(default=[])
