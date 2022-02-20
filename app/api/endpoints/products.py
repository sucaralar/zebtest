from flask import Blueprint
from application import api
from app.api.controllers.products import ns_products

blueprint = Blueprint('products_api', __name__, url_prefix='')

api.add_namespace(ns_products)




