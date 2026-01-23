from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from api.photo_api import photo_router
from api.comment_api import comment_router
from api.user_api import user_router
from api.post_api import post_router
from database import Base, engine
from database.postservice import get_all_posts_db, get_all_user_posts_db
from database.userservice import get_all_or_exact_user
templates = Jinja2Templates(directory="templates")

app = FastAPI(docs_url="/docs")
app.include_router(photo_router)
app.include_router(comment_router)
app.include_router(post_router)
app.include_router(user_router)
Base.metadata.create_all(engine)

@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    all_posts = get_all_posts_db()
    return templates.TemplateResponse(request=request, name="index.html", 
    context={"all_posts": all_posts})

@app.get("/user/{uid}", response_class=HTMLResponse)
async def get_user_html(uid: int, request: Request):
    user = get_all_or_exact_user(uid)
    posts = get_all_user_posts_db(uid)
    return templates.TemplateResponse(request=request, name="user.html", 
    context={"user": user, "user_posts": posts})

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")
    






