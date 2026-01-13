from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from my_twitter.core.models.postgres.models import Base


if TYPE_CHECKING:
    from my_twitter.features.tweet import Tweet
    from my_twitter.features.media import MediaEntity

class Media(Base):
    """
    Модель медиафайла, прикреплённого к твиту.
    При удалении твита медиа удаляются каскадно.
    """
    __tablename__ = "table_media"
    path: Mapped[str] = mapped_column(String(255))
    tweet_id: Mapped[int | None] = mapped_column(ForeignKey("table_tweet.id", ondelete="CASCADE"), nullable=True)
    tweet: Mapped['Tweet'] = relationship("Tweet", back_populates='medias')

    async def to_entity(self) -> "MediaEntity":
        return MediaEntity(
            id_=self.id,
            path=self.path,
            tweet_id=self.tweet_id
        )

    @staticmethod
    async def from_entity(media: "MediaEntity") -> 'Media':
        return Media(
            id=media.id_,
            path=media.path,
            tweet_id=media.tweet_id
        )
