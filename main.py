from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from db import Base, engine, SessionLocal, User, Post

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

# This creates a FastAPI endpoint that returns all users and their posts.
@app.get("/")
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    results = []
    for user in users:
        posts = []
        for post in user.posts:
            posts.append({"title": post.title, "content": post.content})
        results.append({"id": user.id, "username": user.username, "email": user.email, "posts": posts})
    return {"users": results}
