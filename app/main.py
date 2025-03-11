from typing import Annotated

from fastapi import Depends
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.contracts.create_link_api import CreateLinkApi
from app.contracts.link_api import LinkApi
from app.services.exceptions import LinkNotFound, LinkExpired
from app.services.link_service import LinkService

app = FastAPI()


@app.get("/links")
async def get_links(
    link_service: Annotated[LinkService, Depends(LinkService)],
) -> list[LinkApi]:
    return await link_service.get_links()


@app.post("/links")
async def create_link(
    new_link: CreateLinkApi, link_service: Annotated[LinkService, Depends(LinkService)]
) -> LinkApi:
    return await link_service.create_link(new_link)


@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs")


@app.get("/{short_url}")
async def redirect_to_original_url(
    short_url: str, link_service: Annotated[LinkService, Depends(LinkService)]
):
    try:
        original_url = await link_service.get_original_link(short_url)
        redirect_response = RedirectResponse(url=original_url)
        return redirect_response
    except LinkNotFound as e:
        return {"error": str(e)}, 404
    except LinkExpired as e:
        return {"error": str(e)}, 410
