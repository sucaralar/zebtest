from flask import Blueprint
from flask_restx import Api

from app.api.controllers.security import api as security_api

blueprint = Blueprint('security_api', __name__, url_prefix='')

api = Api(blueprint)

api.add_namespace(security_api)