from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.config import DatabaseConfig


async def get_db() -> AsyncGenerator[AsyncSession]:
    config = DatabaseConfig()
    engine = create_async_engine(config.connection_string, pool_pre_ping=True)
    SessionLocal = async_sessionmaker(
        autocommit=False, autoflush=False, bind=engine, expire_on_commit=False
    )

    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
