from sqlalchemy import func

from application import db
from models.base import BaseModel


class SearchedProduct(BaseModel):
    __tablename__ = "searched_products"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    date_registered = db.Column(db.DateTime(timezone=True), server_default=func.now())

