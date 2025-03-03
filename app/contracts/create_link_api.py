from datetime import datetime

from pydantic import BaseModel, AnyHttpUrl


class CreateLinkApi(BaseModel):
    url: AnyHttpUrl
    live_until: datetime | None
