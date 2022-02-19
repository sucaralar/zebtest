from typing import Optional, List
from app.domain.repository import UserRepository, ProductRepository
from app.domain.entity.users import UserIn


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


class ProductManager(ProductRepository):
    ...


