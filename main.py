from fastapi import FastAPI

from db import Base, engine, SessionLocal

# This creates the tables in the database, if they don't already exist.
Base.metadata.create_all(bind=engine)

# This creates a FastAPI instance.
app = FastAPI()

# This creates a dependency that we can use to get a database session.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# This creates a FastAPI endpoint that returns "Hello, world!".
@app.get("/")
def read_root():
    return {"Hello": "World"}
