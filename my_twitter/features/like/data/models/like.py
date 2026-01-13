from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from my_twitter.core.models.postgres.models import Base


if TYPE_CHECKING:
    from my_twitter.features.tweet import Tweet
    from my_twitter.features.user import User
    from my_twitter.features.like import LikeEntity

class Like(Base):
    """
    Модель лайка твита пользователем.
    При удалении твита или пользователя лайк удаляется каскадно.
    """
    __tablename__ = "table_like"
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), primary_key=True)
    tweet_id: Mapped[int] = mapped_column(ForeignKey("table_tweet.id", ondelete="CASCADE"), primary_key=True)

    tweet: Mapped['Tweet'] = relationship("Tweet", back_populates="likes")
    user: Mapped['User'] = relationship("User", back_populates="likes")

    __table_args__ = (UniqueConstraint('user_id', "tweet_id"),)

    def to_entity(self) -> "LikeEntity":
        return LikeEntity(
            user_id=self.user_id,
            tweet_id=self.tweet_id,
        )

    @staticmethod
    def from_entity(entity: "LikeEntity") -> 'Like':
        return Like(
            id=entity.id,
            user_id=entity.user_id,
            tweet_id=entity.tweet_id,
        )
