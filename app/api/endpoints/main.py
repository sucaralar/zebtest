from flask import Blueprint
from flask_restx import Api

from app.api.controllers.main import api as main_api

blueprint = Blueprint('main_api', __name__, url_prefix='')

api = Api(blueprint)

api.add_namespace(main_api)


