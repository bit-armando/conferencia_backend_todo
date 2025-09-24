"""
Database configuration and session management.
Uses SQLite with SQLAlchemy. Exposes Base, engine, and a dependency to acquire DB sessions.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# SQLite URL. The database file will be created in the project root as todos.db
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# For SQLite, it's recommended to set check_same_thread to False when using in multi-threaded contexts like ASGI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    """Base class for SQLAlchemy models."""
    pass


def get_db():
    """FastAPI dependency that yields a database session and ensures it's closed."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
