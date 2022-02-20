
from typing import List
import models
from app.domain.entity.users import UserIn
from app.domain.repository.base import AbstractRepository



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

    def get_admins_emails(self) -> List[str]:
        users = self.list()
        emails = [user.email for user in users]
        return emails


