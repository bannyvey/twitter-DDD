from sqlalchemy import ForeignKey, Table, Column

from my_twitter.core.models.postgres.models import Base

follows = Table(
    "follows",
    Base.metadata,
    Column("follower_id", ForeignKey("user.id"), primary_key=True),
    Column("following_id", ForeignKey("user.id"), primary_key=True)
)
