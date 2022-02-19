from flask_restx import fields


user_serializer = {
    "id": fields.Integer,
    "last_name": fields.String,
    "first_name": fields.String,
    "email": fields.String,
    "password": fields.String,
    "is_active": fields.Boolean,
}