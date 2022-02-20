from flask_restx import abort
from app.domain.repository.user_repository import UserRepository
from app.domain.entity.users import UserIn


class UserManager:

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
        try:
            user_db = self.user_repository.update(_id=user_in.id, obj_in=user_in)
        except Exception as e:
            abort(400, **{"error": "Error trying to update user"})
        return user_db

    def delete(self, user_id: int):
        user_db = self.user_repository.get_by_id(_id=user_id)
        user_db.delete()
        return True

    def get_user_for_token(self, username: str, password: str):
        user_db = self.user_repository.first(criteria={"email": username})
        if not user_db:
            abort(403, **{"error": "Unregistered user"})
        right_password = self.user_repository.verify_password(user=user_db, password=password)
        if right_password:
            user_data = {
                            "id": user_db.id,
                            "last_name": user_db.last_name,
                            "first_name": user_db.first_name,
                            "email": user_db.first_name,
                         }
        else:
            abort(401, **{"error": "Your logins are incorrect"})
        return user_data




