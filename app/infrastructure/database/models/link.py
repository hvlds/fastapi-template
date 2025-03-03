from datetime import datetime

from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped

from app.infrastructure.database.models.base import Base


class Link(Base):
    __tablename__ = "link"
    __table_args__ = {"schema": "link_shortener"}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    url: Mapped[str]
    short_url: Mapped[str] = mapped_column(String, unique=True, index=True)
    created_at: Mapped[datetime]
    live_until: Mapped[datetime | None]
