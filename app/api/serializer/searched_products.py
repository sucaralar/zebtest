from flask_restx import fields


searched_product_serializer = {
    "id": fields.Integer,
    "product_id": fields.Integer,
    "date_registered": fields.DateTime(dt_format='rfc822')
}

total_searched_product_serializer = {
    "total_searches": fields.Integer,
}