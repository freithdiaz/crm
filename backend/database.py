from sqlmodel import create_engine, SQLModel, Session
from typing import Generator
import os

DATABASE_URL = "sqlite:///./crm.db"

# Optimized engine configuration with connection pooling
engine = create_engine(
    DATABASE_URL,
    echo=False,  # Disable SQL logging in production for better performance
    pool_pre_ping=True,  # Enable connection health checks
    pool_size=10,  # Maintain a pool of 10 connections
    max_overflow=20  # Allow up to 20 additional connections
)

def get_session() -> Generator[Session, None, None]:
    """Database session generator with proper cleanup."""
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
