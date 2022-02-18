from app.domain.repository import UserRepository, ProductRepository

from app.domain.entity import UserIn, UserOut


class UserManager:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create(self, user_in: UserIn) -> UserOut:
        user_db = self.user_repository.create(obj_in=user_in)
        return user_db


class ProductManager(ProductRepository):
    ...


