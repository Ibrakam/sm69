from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from jose import jwt
from api.photo_api import photo_router
from api.comment_api import comment_router
from api.user_api import user_router
from api.post_api import post_router
from database import Base, engine
from database.postservice import get_all_posts_db, get_all_user_posts_db
from database.userservice import get_all_or_exact_user, get_user_by_username_db
from schemas import TokenSchema, UserSchema
from deps import get_current_user, _credentials_exception
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta, datetime
from typing import Optional
from config import access_token_exp_min, secret_key, algorithm



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
    

def verify_password(password, password_db):
    return password == password_db


async def create_access_token(data):
    to_encode = data.copy()
    
    expire = datetime.utcnow() + timedelta(minutes=access_token_exp_min)
    
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)

    return encoded_jwt


@app.post("/token", response_model=TokenSchema)
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user = get_user_by_username_db(form.username)
    if not form.username and verify_password(form.username, user.password):
        return _credentials_exception()
    
    access_token = await create_access_token(data={"sub": user.username})
    return {"access_token": access_token,
            "token_type": "bearer"}

@app.get("/user/me")
async def get_user(user: UserSchema = Depends(get_current_user)):
    return user






@app.post("/login", response_class=HTMLResponse)
async def login_form(username: str = Form(...),
                    password: str = Form(...)):
    
    user = get_user_by_username_db(username)
    if not username and verify_password(password, user.password):
        return _credentials_exception()
    
    token = create_access_token(data={"sub": user.username})

    response = RedirectResponse(url="/", status_code=303)
    print(await token)
    response.set_cookie(
        key="access_token",
        value=f"Bearer {token}",
        httponly=True,
        samesite="lax",
        max_age=30
    )
    return response


                                                                                           






