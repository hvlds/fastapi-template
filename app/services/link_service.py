from typing import Annotated
from fastapi import Depends

from app.contracts.link_api import LinkApi
from app.infrastructure.repositories.link_repository import LinkRepository
from app.mappers.link_api_mapper import LinkApiMapper


class LinkService:
    def __init__(
        self, link_repository: Annotated[LinkRepository, Depends(LinkRepository)]
    ):
        self.link_repository = link_repository

    def get_links(self) -> list[LinkApi]:
        all_db_links = self.link_repository.get_links()
        return [LinkApiMapper.map(db_link) for db_link in all_db_links]
