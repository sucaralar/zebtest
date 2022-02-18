from flask import Blueprint
from flask_restx import Api
from app.api.controllers.products import api as products_api

blueprint = Blueprint('products_api', __name__, url_prefix='')

api = Api(blueprint)

api.add_namespace(products_api)
