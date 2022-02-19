from application import db
from models.base import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash


class User(BaseModel):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, index=True)
    last_name = db.Column(db.String)
    first_name = db.Column(db.String)
    email = db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String)
    is_active = db.Column(db.Boolean, default=True)

    def __init__(self, last_name: str, first_name: str, password: str, email: str, is_active: bool):
        self.last_name = last_name
        self.first_name = first_name
        self.password = generate_password_hash(password)
        self.email = email
        self.is_active = is_active

    def verify_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)

