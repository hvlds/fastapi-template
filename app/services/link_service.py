import string
import random
from datetime import datetime, UTC
from typing import Annotated
from uuid import uuid4

from fastapi import Depends

from app.contracts.create_link_api import CreateLinkApi
from app.contracts.link_api import LinkApi
from app.infrastructure.repositories.link_repository import LinkRepository
from app.mappers.link_api_mapper import LinkApiMapper
from app.services.exceptions import LinkNotFound, LinkExpired


class LinkService:
    def __init__(
        self, link_repository: Annotated[LinkRepository, Depends(LinkRepository)]
    ):
        self.link_repository = link_repository

    async def get_links(self) -> list[LinkApi]:
        all_db_links = await self.link_repository.get_links()
        return [LinkApiMapper.map(db_link) for db_link in all_db_links]

    async def get_original_link(self, short_url: str) -> str:
        now = datetime.now(tz=UTC)
        db_link = await self.link_repository.get_link_by_short_url(short_url)
        if not db_link:
            raise LinkNotFound(short_url)

        if db_link.live_until and db_link.live_until < now:
            raise LinkExpired(short_url)

        return db_link.url

    async def create_link(self, new_link: CreateLinkApi) -> LinkApi:
        db_link = await self.link_repository.create_link(
            url=new_link.url.unicode_string(),
            short_url=LinkService._generate_short_id(seed=str(uuid4())),
            live_until=new_link.live_until,
        )
        return LinkApiMapper.map(db_link)

    @staticmethod
    def _generate_short_id(seed: str, length=6):
        """Generate a random short ID of specified length using Base62 encoding."""
        random.seed(seed)
        base62_chars = string.digits + string.ascii_letters
        return "".join(random.choice(base62_chars) for _ in range(length))
