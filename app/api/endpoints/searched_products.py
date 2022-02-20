from flask import Blueprint
from application import api
from app.api.controllers.searched_products import ns_searched_products

blueprint = Blueprint('searched_products_api', __name__, url_prefix='')

api.add_namespace(ns_searched_products)
