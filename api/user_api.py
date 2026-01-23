from fastapi import APIRouter
from database.userservice import *

user_router = APIRouter(prefix="/user", tags=["User API"])


@user_router.get("/get_all_or_exact_user")
async def get_all_or_exact_user_api(uid: int):
    result = get_all_or_exact_user(uid=uid)
    if result:
        return {"status": True, "message": result}
    return {"status": False, "message": result}


@user_router.post("/create_user")
async def create_user_api(user: UserSchema):
    result = create_user_db(user=user)
    if result:
        return {"status": True, "message": result}
    return {"status": False, "message": result}


@user_router.delete("/delete_user")
async def delete_user_api(uid: int):
    result = delete_user_db(uid=uid)
    if result:
        return {"status": True, "message": result}
    return {"status": False, "message": result}


@user_router.put("/update_user")
async def update_user_api(uid: int, change_data: str, new_data: str):
    result = update_user_db(uid=uid, change_data=change_data, new_data=new_data)
    if result:
        return {"status": True, "message": result}
    return {"status": False, "message": result}