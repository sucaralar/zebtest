from app.domain.repository import UserRepository, ProductRepository
from app.domain.entity.products import ProductBase
from app.utils.notify.send_email import EmailNotification
from app.utils.notify.providers import SendGridNotification


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
        notify = EmailNotification(provider=SendGridNotification)
        email_send = notify.send(to_emails=emails,
                                 subject="Notification from Zebtest by Su Carrillo",
                                 html_content=html_content)
        return product_db

    def delete(self, product_id: int):
        product_db = self.product_repository.get_by_id(_id=product_id)
        product_db.delete()
        return True


