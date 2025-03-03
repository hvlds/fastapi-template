from typing import Annotated

from fastapi import APIRouter, Depends

from app.contracts.create_link_api import CreateLinkApi
from app.contracts.link_api import LinkApi
from app.services.link_service import LinkService

router = APIRouter(
    prefix="/links",
    tags=["links"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_links(
    link_service: Annotated[LinkService, Depends(LinkService)],
) -> list[LinkApi]:
    return link_service.get_links()


@router.post("/")
def create_link(
    new_link: CreateLinkApi, link_service: Annotated[LinkService, Depends(LinkService)]
) -> LinkApi:
    return link_service.create_link(new_link)
