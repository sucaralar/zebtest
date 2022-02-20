from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    """common properties for model use"""
    last_name: str
    first_name: str
    email: str

    class Config:
        orm_mode = True


class UserIn(UserBase):
    """For PUT/POST requests"""
    id: Optional[int]
    password: str


class UserOut(UserBase):
    """For retrieving existing user(s)"""
    id: int

    class Config:
        orm_mode = True
