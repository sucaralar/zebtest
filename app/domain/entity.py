from decimal import Decimal

from pydantic import BaseModel
from typing import Optional


# ==================================================================
# User Entities
# ==================================================================
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


# ==================================================================
# Product Entities
# ==================================================================
class ProductBase(BaseModel):
    """common properties for model use"""
    sku: str
    name: str
    price: Decimal
    brand: str
    description: str

    class Config:
        orm_mode = True


class ProductOut(ProductBase):
    """For retrieving existing product(s)"""
    id: int

    class Config:
        orm_mode = True


# ==================================================================
# Product Entities
# ==================================================================
class LoginBase(BaseModel):
    """For get-token existing product(s)"""
    username: str

    class Config:
        orm_mode = True
