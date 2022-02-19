from flask_restx import fields


product_serializer = {
    "id": fields.Integer,
    "sku": fields.String,
    "name": fields.String,
    "price": fields.Decimal,
    "brand": fields.String,
    "description": fields.String,
    "qty": fields.Integer,
    "is_active": fields.Boolean,
}