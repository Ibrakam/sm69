from fastapi import APIRouter
from database.postservice import *
from api import result_message

post_router = APIRouter(prefix="/post")



@post_router.post("/create_post")
async def create_post_api(post: UserPostSchema):
    result = create_post_db(post=post)
    if result:
        return {"status": True, "message": result}
    return {"status": False, "message": result}


@post_router.get("/get_user_all_posts")
async def get_user_all_posts(uid: int):
    result = get_all_user_posts_db(uid=uid)
    if result:
        return {"status": True, "message": result}
    return {"status": False, "message": result}


@post_router.get("/get_all_posts")
async def get_all_posts():
    result = get_all_posts_db()
    if result:
        return {"status": True, "message": result}
    return {"status": False, "message": result}


@post_router.get("/get_exact_post/{pid}")
async def get_exact_post_pid_api(pid: int):
    result = get_exact_post_db(pid)
    return result_message(result)


@post_router.put('/edit_post/{pid}')
async def edit_post_api(pid: int, text: str):
    result = edit_post_db(pid, text)
    return result_message(result)


@post_router.delete('/delete_post/{pid}')
async def delete_post_api(pid: int):
    result = delete_post_db(pid)
    return result_message(result)