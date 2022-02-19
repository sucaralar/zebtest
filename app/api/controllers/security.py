from flask_restx import Namespace, Resource, abort
from flask_jwt_extended import create_access_token
from app.domain.manager import UserManager
from app.domain.entity.security import LoginBase
from app.api.serializer.security import jwt_serializer

api = Namespace('securtity', path="/security/", description='Security Endpoint')

login_schema = api.schema_model(LoginBase.__name__, LoginBase.schema())
jwt_model = api.model('JWTModel', jwt_serializer)


class GetTokenResource(Resource):
    @api.doc('Get-Token')
    @api.expect(login_schema)
    @api.marshal_with(jwt_model)
    def post(self):
        """ get token endpoint """
        manager = UserManager()
        username = api.payload.get("username")
        password = api.payload.get("password")
        token_data = manager.get_user_for_token(username=username, password=password)
        access_token = create_access_token(identity=token_data)
        return {"jwt": access_token}


# Register resource
api.add_resource(GetTokenResource, '/get-token', endpoint='get-token', methods=['POST'])