from flask import Blueprint
from application import api
from app.api.controllers.users import ns_users

blueprint = Blueprint('user_api', __name__, url_prefix='')

api.add_namespace(ns_users)




