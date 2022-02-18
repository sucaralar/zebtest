from application import db
from models.base import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, index=True)
    last_name = db.Column(db.String)
    first_name = db.Column(db.String)
    email = db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String)
    is_active = db.Column(db.Boolean, default=True)