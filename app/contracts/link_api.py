from datetime import datetime
from pydantic import BaseModel


class LinkApi(BaseModel):
    url: str
    short_url: str
    created_at: datetime
    live_until: datetime | None
