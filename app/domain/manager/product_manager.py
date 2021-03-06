from flask_restx import abort
from app.domain.repository.product_repository import ProductRepository
from app.domain.repository.user_repository import UserRepository
from app.domain.repository.searched_product_repository import SearchedProductRepository
from app.domain.entity.products import ProductBase
from app.domain.entity.searched_product import SearchedProductBase
from app.utils.notify.send_email import EmailNotification
from app.utils.notify.providers import SendGridNotification
import models


class ProductManager:

    def __init__(self):
        self.product_repository = ProductRepository()

    def get_list(self):
        products = self.product_repository.list()
        return products

    def get_by_id(self, product_id: int, user: models.User):
        searched_product_repository = SearchedProductRepository()
        product_db = self.product_repository.get_by_id(_id=product_id)
        # check if is an anonymous user
        if product_db and not user:
            searched_product_in = SearchedProductBase(**{"product_id": product_id})
            searched_product_repository.create(obj_in=searched_product_in)
        return product_db

    def create(self, product_in: ProductBase):
        product_db = self.product_repository.create(obj_in=product_in)
        return product_db

    def update(self, product_in: ProductBase):
        product = self.product_repository.get_by_id(_id=product_in.id)
        if not product:
            abort(404, **{"error": "Product not found"})
        html_content = f'<strong>The product #{product.id} has been modified</strong><ul><li> Sku: {product.sku} -> {product_in.sku}</li><li> Name: {product.name} -> {product_in.name}</li><li> Price: {product.price} -> {product_in.price}</li><li> Brand: {product.brand} -> {product_in.brand}</li><li> Description: {product.description} -> {product_in.description}</li><li> Qty: {product.qty} -> {product_in.qty}</li></ul> <br><span>Zeb test wishes you a good day.</span>'
        try:
            product_db = self.product_repository.update(_id=product_in.id, obj_in=product_in)
        except Exception as e:
            abort(400, **{"error": "Error trying to update product"})
        user_repository = UserRepository()
        emails = user_repository.get_admins_emails()
        if emails:
            notify = EmailNotification(provider=SendGridNotification)
            email_send = notify.send(to_emails=emails,
                                     subject="Notification from Zebtest by Su Carrillo",
                                     html_content=html_content)
        return product_db

    def delete(self, product_id: int):
        product_db = self.product_repository.get_by_id(_id=product_id)
        product_db.delete()
        return True


