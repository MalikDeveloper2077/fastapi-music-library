from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, constr


class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr
    password: str
    is_company: bool
    created_at: datetime


class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=6)
    is_company: bool = False
