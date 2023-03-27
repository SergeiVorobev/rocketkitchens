from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# This is the database URL that we'll use for connecting to the database.
# Change this to your own database URL.
SQLALCHEMY_DATABASE_URL = "sqlite:///example.db"

# This creates the engine that we'll use to connect to the database.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# This creates the base class that we'll use for our database models.
Base = declarative_base()

# This creates a SessionLocal class that we'll use to create database sessions.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
