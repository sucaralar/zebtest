
from typing import List
import models
from app.domain.entity.searched_product import SearchedProductBase
from app.domain.repository.base import AbstractRepository


class SearchedProductRepository(AbstractRepository):
    model = models.SearchedProduct

    def create(self, obj_in: SearchedProductBase) -> models.SearchedProduct:
        new_obj = models.SearchedProduct(product_id=obj_in.product_id)
        new_obj.create()
        return new_obj