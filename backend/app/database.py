#Database configuration for the FastAPI app.
#Uses AsyncSession for async database operations.
#Creates an engine and session factory for database connections.
#Provides a dependency for getting a database session.
#Manages PostgreSQL database connection using SQLAlchemy.

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database URL from .env file
DATABASE_URL = os.getenv("DATABASE_URL")

# Create an async database engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create a session factory
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, autocommit=False, autoflush=False)

# Base class for database models
Base = declarative_base()

# Dependency to get a database session
async def get_db():
    async with SessionLocal() as session:
        yield session
