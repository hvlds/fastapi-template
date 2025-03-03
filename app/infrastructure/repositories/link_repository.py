from datetime import datetime, UTC
from typing import Annotated

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.infrastructure.database.models.link import Link
from app.infrastructure.database.utils import get_db


class LinkRepository:
    def __init__(self, db_session: Annotated[Session, Depends(get_db)]):
        self.session = db_session

    def get_links(self) -> list[Link]:
        stmt = select(Link)
        result = self.session.execute(stmt).scalars().all()
        return [link for link in result]

    def create_link(
        self, url: str, short_url: str, live_until: datetime | None
    ) -> Link:
        new_link = Link(
            url=url,
            short_url=short_url,
            live_until=live_until,
            created_at=datetime.now(tz=UTC),
        )
        self.session.add(new_link)
        self.session.commit()
        return new_link
