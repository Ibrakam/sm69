from fastapi import FastAPI
from api.photo_api import photo_router
from api.comment_api import comment_router
from database import Base, engine


app = FastAPI(docs_url="/docs")
app.include_router(photo_router)
app.include_router(comment_router)
Base.metadata.create_all(engine)