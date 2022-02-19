from typing import Any
from app.domain.repository import UserRepository, ProductRepository
from app.domain.entity.users import UserIn
from app.domain.entity.products import ProductBase
from app.utils.notify import Notify



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
        right_password = self.user_repository.verify_password(user=user_db, password=password)
        if right_password:
            user_data = {
                            "id": user_db.id,
                            "last_name": user_db.last_name,
                            "first_name": user_db.first_name,
                            "email": user_db.first_name,
                         }
        # TODO return exception if password isn't right
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
        product_db = self.product_repository.create(obj_in=product_in)
        return product_db

    def update(self, product_in: ProductBase):
        product = self.product_repository.get_by_id(_id=product_in.id)
        html_content = f'<strong>The product #{product.id} has been modified</strong><ul><li> Sku: {product.sku} -> {product_in.sku}</li><li> Name: {product.name} -> {product_in.name}</li><li> Price: {product.price} -> {product_in.price}</li><li> Brand: {product.brand} -> {product_in.brand}</li><li> Description: {product.description} -> {product_in.description}</li><li> Qty: {product.qty} -> {product_in.qty}</li></ul> <br><span>Zeb test wishes you a good day.</span>'

        product_db = self.product_repository.update(_id=product_in.id, obj_in=product_in)
        user_repository = UserRepository()
        emails = user_repository.get_admins_emails()
        notify = Notify(emails=emails,
                        subject="Notification from Zebtest by Su Carrillo",
                        html_content=html_content)
        notify.send()
        return product_db

    def delete(self, product_id: int):
        product_db = self.product_repository.get_by_id(_id=product_id)
        product_db.delete()
        return True


