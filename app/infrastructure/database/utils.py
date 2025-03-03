from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.config import DatabaseConfig


def get_db() -> Iterator[Session]:
    config = DatabaseConfig()
    engine = create_engine(config.connection_string, pool_pre_ping=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
