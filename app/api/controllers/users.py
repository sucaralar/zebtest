from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required
from app.domain.entity import UserIn
from app.domain.manager import UserManager

api = Namespace('users', path="/users/", description='User Endpoint')


class UserResource(Resource):
    @jwt_required()
    def get(self, user_id: int = None):
        """ Endpoint to get an user(s) """
        if user_id:
            # user_manager = UserManager()
            # response = user_manager.get_by_id(id=id)
            response = {}
        else:
            response = []
            # response = user_rep.list()
        return response

    @jwt_required()
    def post(self, user_in: UserIn):
        """ Create new user """
        return {}

    @jwt_required()
    def put(self, user_id: int, user_in: UserIn):
        """ Update update a existent user """
        return {}

    @jwt_required()
    def delete(self, user_id: int):
        """ Delete update a existent user """
        return {}


# Register resource
api.add_resource(UserResource, '/', endpoint='user-list', methods=['GET'])
api.add_resource(UserResource, '/<int:user_id>', endpoint='user-get', methods=['GET'])
api.add_resource(UserResource, '/', endpoint='user-update', methods=['PUT'])
api.add_resource(UserResource, '/', endpoint='user-delete', methods=['DELETE'])
