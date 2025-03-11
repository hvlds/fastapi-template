from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database.models.link import Link


async def test_create_link_works(test_client, test_db_session: AsyncSession):
    # GIVEN
    new_url = "https://www.example.com/"

    # Check that the link does not exist
    exists_stmt = select(Link).where(Link.url == new_url)
    result = (await test_db_session.execute(exists_stmt)).fetchone()
    assert result is None

    # WHEN
    response = test_client.post("/links", json={"url": new_url, "live_until": None})

    # THEN
    link = response.json()
    assert link["url"] == new_url
    assert link["short_url"] is not None
    assert link["created_at"] is not None

    # Check that the link exists
    result = (await test_db_session.execute(exists_stmt)).fetchone()
    assert result is not None
    db_link = result[0]
    assert db_link.url == new_url
    assert db_link.short_url == link["short_url"]
