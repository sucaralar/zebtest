from flask import Blueprint
from flask_restx import Api

from app.api.controllers.users import api as users_api

blueprint = Blueprint('user_api', __name__, url_prefix='')

api = Api(blueprint)

api.add_namespace(users_api)
