from typing import Annotated

from fastapi import FastAPI, Depends
from starlette.responses import RedirectResponse

from app.routers import links
from app.services.exceptions import LinkNotFound
from app.services.link_service import LinkService

app = FastAPI()

app.include_router(links.router)


@app.get("/{short_url}")
def redirect_to_original_url(
    short_url: str, link_service: Annotated[LinkService, Depends(LinkService)]
):
    try:
        original_url = link_service.get_original_link(short_url)
        redirect_response = RedirectResponse(url=original_url)
        return redirect_response
    except LinkNotFound as e:
        return {"error": str(e)}
