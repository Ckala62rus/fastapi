from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from core.config import settings

# SQLALCHEMY_DATABASE_URL = "postgresql://pguser:000000@localhost:5432/postgres"
# SQLALCHEMY_DATABASE_URL = "postgresql://pguser:000000@localhost:5432/postgres"
SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_DATABASE_URL_FOR_ALEMBIC

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


async_engine = create_async_engine(
    url=settings.SQLALCHEMY_DATABASE_URL,
    # url="postgresql+psycopg://pguser:000000@localhost:5432/mydb",
    echo=True,
    # pool_size=5,
    # max_overflow=10
)
SessionLocal = async_sessionmaker(async_engine)

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
