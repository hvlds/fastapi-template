import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.pool import StaticPool

from app.infrastructure.database.models.base import Base
from app.infrastructure.database.utils import get_db
from app.main import app


@pytest.fixture(scope="function")
async def test_db_session():
    """Create a new database session with a rollback at the end of the test."""
    SQLITE_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

    # Create an async engine
    engine = create_async_engine(
        SQLITE_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    # Create a sessionmaker for async sessions
    TestingSessionLocal = async_sessionmaker(
        bind=engine, class_=AsyncSession, expire_on_commit=False
    )

    # Create tables asynchronously
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Create an async session
    async with TestingSessionLocal() as session:
        yield session  # Provide the session to the test

    # Cleanup
    await engine.dispose()


@pytest.fixture(scope="function")
def test_client(test_db_session):
    """Create a test client with an overridden dependency for DB session."""

    async def override_get_db():
        async with test_db_session as session:
            yield session

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as client:
        yield client
