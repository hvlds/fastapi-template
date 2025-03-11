from datetime import datetime, UTC
from typing import Annotated

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database.models.link import Link
from app.infrastructure.database.utils import get_db


class LinkRepository:
    def __init__(self, db_session: Annotated[AsyncSession, Depends(get_db)]):
        self.session = db_session

    async def get_links(self) -> list[Link]:
        stmt = select(Link)
        result = (await self.session.execute(stmt)).scalars().all()
        return [link for link in result]

    async def get_link_by_short_url(self, short_url: str) -> Link | None:
        stmt = select(Link).where(Link.short_url == short_url)
        result = (await self.session.execute(stmt)).scalar()
        return result

    async def create_link(
        self, url: str, short_url: str, live_until: datetime | None
    ) -> Link:
        new_link = Link(
            url=url,
            short_url=short_url,
            live_until=live_until,
            created_at=datetime.now(tz=UTC),
        )
        self.session.add(new_link)
        await self.session.commit()
        return new_link
