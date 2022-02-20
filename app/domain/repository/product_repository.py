import models
from app.domain.repository.base import AbstractRepository
from app.domain.entity.products import ProductBase


class ProductRepository(AbstractRepository):
    model = models.Product

    def create(self, obj_in: ProductBase) -> models.Product:
        new_obj = models.Product(sku=obj_in.sku,
                                 name=obj_in.name,
                                 price=obj_in.price,
                                 brand=obj_in.brand,
                                 description=obj_in.description,
                                 qty=obj_in.qty,
                                 is_active=obj_in.is_active)
        new_obj.create()
        return new_obj

    def delete(self, obj_db: models.Product):
        obj_db.is_active = False
        obj_db.update()
        return obj_db
