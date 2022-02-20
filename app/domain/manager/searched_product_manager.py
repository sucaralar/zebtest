from app.domain.repository.searched_product_repository import SearchedProductRepository
from app.domain.entity.searched_product import SearchedProductBase


class SearchedProductManager:

    def __init__(self):
        self.searched_product_repository = SearchedProductRepository()

    def create(self, searched_in: SearchedProductBase):
        searched_product_db = self.searched_product_repository.create(obj_in=searched_in)
        return searched_product_db

    def get_searched(self, product_id: int) -> int:
        filter_data = {"product_id": product_id}
        searched = self.searched_product_repository.filter_by(filter_data)
        total = len(searched)
        return total



