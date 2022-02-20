from flask import Blueprint
from application import api
from app.api.controllers.security import api as security_api

blueprint = Blueprint('security_api', __name__, url_prefix='')

api.add_namespace(security_api)


