from application import db
from models.base import BaseModel


class Product(BaseModel):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, index=True)
    sku = db.Column(db.String, unique=True, index=True)
    name = db.Column(db.String)
    price = db.Column(db.Numeric)
    brand = db.Column(db.String)
    description = db.Column(db.String)
    qty = db.Column(db.Integer)
    is_active = db.Column(db.Boolean, default=True)