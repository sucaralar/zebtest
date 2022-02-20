from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required
from app.domain.entity.users import UserIn
from app.domain.manager import UserManager
from app.api.serializer.users import user_serializer

ns_users = Namespace('users', path="/", description='User Endpoint')

users_schema = ns_users.schema_model('UserRequest', UserIn.schema())
user_model = ns_users.model('UserResponse', user_serializer)


class UserResource(Resource):
    @jwt_required()
    @ns_users.marshal_with(user_model)
    def get(self, user_id: int = None):
        """ Endpoint to get an user(s) """
        manager = UserManager()
        if user_id:
            response = manager.get_by_id(user_id=user_id)
        else:
            response = manager.get_list()
        return response

    @jwt_required()
    @ns_users.marshal_with(user_model)
    @ns_users.expect(users_schema)
    def post(self):
        """ Create new user """
        manager = UserManager()
        user_in = UserIn(**ns_users.payload)
        response = manager.create(user_in=user_in)
        return response

    @jwt_required()
    @ns_users.marshal_with(user_model)
    @ns_users.expect(users_schema)
    def put(self):
        """ Update update a existent user """
        manager = UserManager()
        user_in = UserIn(**ns_users.payload)
        response = manager.update(user_in=user_in)
        return response

    @jwt_required()
    def delete(self, user_id: int):
        """ Delete update a existent user """
        manager = UserManager()
        response = manager.delete(user_id=user_id)
        return {"deleted": response}


# Register resource
ns_users.add_resource(UserResource, '/users', methods=['GET', 'POST', 'PUT'])
ns_users.add_resource(UserResource, '/users/<int:user_id>',  methods=['GET', 'DELETE'])

