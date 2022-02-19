import json
from flask import Blueprint
from flask_restx import Api
from werkzeug.exceptions import HTTPException
from app.api.controllers.users import api as users_api

blueprint = Blueprint('user_api', __name__, url_prefix='')

api = Api(blueprint)

api.add_namespace(users_api)


@api.errorhandler(HTTPException)
def handle_error(error: HTTPException):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = error.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": error.code,
        "description": error.description,
    })
    response.content_type = "application/json"
    return response


