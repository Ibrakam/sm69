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