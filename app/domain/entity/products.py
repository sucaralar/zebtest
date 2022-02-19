from decimal import Decimal

from pydantic import BaseModel


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


