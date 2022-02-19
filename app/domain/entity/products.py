from typing import Optional
from decimal import Decimal

from pydantic import BaseModel


# ==================================================================
# Product Entities
# ==================================================================
class ProductBase(BaseModel):
    """common properties for model use"""
    id: Optional[int]
    sku: str
    name: str
    price: Decimal
    brand: str
    description: str
    qty: int
    is_active: bool

    class Config:
        orm_mode = True


class ProductOut(ProductBase):
    """For retrieving existing product(s)"""
    id: int

    class Config:
        orm_mode = True


