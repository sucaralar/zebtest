from app.domain.repository import UserRepository, ProductRepository
from app.domain.entity.users import UserIn, UserOut
from app.domain.entity.products import ProductBase


class UserManager:
    user_repository = None

    def __init__(self):
        self.user_repository = UserRepository()

    def get_list(self):
        users = self.user_repository.list()
        return users

    def get_by_id(self, user_id: int):
        user_db = self.user_repository.get_by_id(_id=user_id)
        return user_db

    def create(self, user_in: UserIn):
        user_db = self.user_repository.create(obj_in=user_in)
        return user_db

    def update(self, user_in: UserIn):
        user_db = self.user_repository.update(_id=user_in.id, obj_in=user_in)
        return user_db

    def delete(self, user_id: int):
        user_db = self.user_repository.get_by_id(_id=user_id)
        user_db.delete()
        return True

    def get_user_for_token(self, username: str, password: str):
        user_db = self.user_repository.first(criteria={"email": username})
        user_data = {
                        "id": user_db.id,
                        "last_name": user_db.last_name,
                        "first_name": user_db.first_name,
                        "email": user_db.first_name,
                     }
        return user_data


class ProductManager(ProductRepository):
    product_repository = ProductRepository

    def __init__(self):
        self.product_repository = ProductRepository()

    def get_list(self):
        products = self.product_repository.list()
        return products

    def get_by_id(self, product_id: int):
        product_db = self.product_repository.get_by_id(_id=product_id)
        return product_db

    def create(self, product_in: ProductBase):
        user_db = self.product_repository.create(obj_in=product_in)
        return user_db

    def update(self, product_in: ProductBase):
        user_db = self.product_repository.update(_id=product_in.id, obj_in=product_in)
        return user_db

    def delete(self, product_id: int):
        user_db = self.product_repository.get_by_id(_id=product_id)
        user_db.delete()
        return True


