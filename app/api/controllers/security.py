from flask_restx import Namespace, Resource, abort
from app.domain.entity import UserOut, LoginBase
from flask_jwt_extended import create_access_token

api = Namespace('securtity', path="/security/", description='Security Endpoint')

login_schema = api.schema_model(LoginBase.__name__, LoginBase.schema())


class GetTokenResource(Resource):
    @api.doc('Get-Token')
    @api.expect(login_schema)
    def post(self):
        """ get token endpoint """
        username = api.payload.get("username")
        password = api.payload.get("password")

        access_token = create_access_token(identity=username)
        return {"jwt": access_token}


# Register resource
api.add_resource(GetTokenResource, '/get-token', endpoint='products-list', methods=['POST'])