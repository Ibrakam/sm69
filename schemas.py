from pydantic import BaseModel
from typing import Optional




class UserSchema(BaseModel):
    phone_number: str
    password: str
    email: str
    username: str
    name: str
    surname: Optional[str] = None
    city: Optional[str] = None
    date_of_birth: Optional[str] = None


class UserPostSchema(BaseModel):
    main_text: str
    uid: int


class PhotoPostSchema(BaseModel):
    photo_path: str
    pid: int


class CommentSchema(BaseModel):
    text: str
    uid: int
    pid: int


class ResultSchema(BaseModel):
    status: int
    message: bool


class TokenSchema(BaseModel):
    access_token: str
    token_type: str
