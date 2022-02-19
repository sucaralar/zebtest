from app.api.shared.global_exceptions import NotFoundError
from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required
from app.domain.entity.users import UserIn
from app.domain.manager import UserManager
from app.api.serializer.users import user_serializer

api = Namespace('users', path="/", description='User Endpoint')

users_schema = api.schema_model(UserIn.__name__, UserIn.schema())
user_model = api.model('UserModel', user_serializer)


class UserResource(Resource):
    @jwt_required()
    @api.marshal_with(user_model)
    def get(self, user_id: int = None):
        """ Endpoint to get an user(s) """
        manager = UserManager()
        if user_id:
            response = manager.get_by_id(user_id=user_id)
        else:
            response = manager.get_list()
        return response

    @jwt_required()
    @api.marshal_with(user_model)
    @api.expect(users_schema)
    def post(self):
        """ Create new user """
        manager = UserManager()
        user_in = UserIn(**api.payload)
        response = manager.create(user_in=user_in)
        return response

    @jwt_required()
    @api.marshal_with(user_model)
    @api.expect(users_schema)
    def put(self):
        """ Update update a existent user """
        manager = UserManager()
        user_in = UserIn(**api.payload)
        response = manager.update(user_in=user_in)
        return response

    @jwt_required()
    def delete(self, user_id: int):
        """ Delete update a existent user """
        manager = UserManager()
        response = manager.delete(user_id=user_id)
        return {"deleted": response}


# Register resource
api.add_resource(UserResource, '/users', endpoint='user-list', methods=['GET'])
api.add_resource(UserResource, '/users/<int:user_id>', endpoint='user-get', methods=['GET'])
api.add_resource(UserResource, '/users', endpoint='user-create', methods=['POST'])
api.add_resource(UserResource, '/users', endpoint='user-update', methods=['PUT'])
api.add_resource(UserResource, '/users/<int:user_id>', endpoint='user-delete', methods=['DELETE'])
