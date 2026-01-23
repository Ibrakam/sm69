from fastapi import APIRouter
from database.commentservice import *
from schemas import CommentSchema, ResultSchema
from api import result_message


comment_router = APIRouter(prefix="/comment", tags=["Comment API"])


@comment_router.post("/add_comment")
async def add_comment_api(comment: CommentSchema):
    result = add_comment_db(comment)
    return result_message(result)


@comment_router.get("/get_post_comments", response_model=ResultSchema)
async def get_post_comment_api(pid: int):
    result = get_all_comments_exact_post_db(pid)
    return result_message(result)


@comment_router.get("/get_all_comments")
async def get_all_comments_api():
    result = get_all_comments_db()
    return result_message(result)




