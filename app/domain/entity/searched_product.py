from typing import Optional

from pydantic import BaseModel


class SearchedProductBase(BaseModel):
    id: Optional[int]
    product_id: int


    class Config:
        orm_mode = True