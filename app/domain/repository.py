import abc
from typing import Any, List
import models
from app.domain.entity.users import UserIn
from app.domain.entity.products import ProductBase


class AbstractRepository(abc.ABC):
    model = None

    def create(self, obj: Any) -> Any:
        return self.model.create()

    def first(self, criteria: dict) -> Any:
        return self.model.first(criteria=criteria)

    def filter_by(self, criteria: Any) -> Any:
        return self.model.filter_by(**criteria)

    def get_by_id(self, _id: int) -> Any:
        return self.model.get_by_id(_id=_id)

    def update(self, _id: int, obj_in: Any) -> Any:
        data = obj_in.dict(exclude_unset=True)
        obj = self.model.get_by_id(_id=_id)
        return obj.update(data=data)

    def list(self) -> List[Any]:
        return self.model.list()

    def delete(self, _id: Any):
        obj = self.model.get_by_id(_id=_id)
        return obj.delete()


class UserRepository(AbstractRepository):
    model = models.User

    def create(self, obj_in: UserIn) -> models.User:
        new_obj = models.User(last_name=obj_in.last_name,
                              first_name=obj_in.first_name,
                              email=obj_in.email,
                              password=obj_in.password,
                              is_active=True)
        new_obj.create()
        return new_obj

    def verify_password(self, user: models.user, password: str):
        is_the_same = user.verify_password(password=password)
        return is_the_same


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
