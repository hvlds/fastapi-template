from app.contracts.link_api import LinkApi
from app.infrastructure.database.models.link import Link


class LinkApiMapper:
    @staticmethod
    def map(db_link: Link) -> LinkApi:
        return LinkApi(
            url=db_link.url,
            short_url=db_link.short_url,
            created_at=db_link.created_at,
            live_until=db_link.live_until,
        )
