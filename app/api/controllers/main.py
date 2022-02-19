from flask_restx import Namespace, Resource

api = Namespace('main_api', path="/", description='Main Endpoint')


class HelloWorldResorce(Resource):
    # @api.doc('Hello World!')
    def get(self):
        """ root endpoint, hello world """
        return {"hello": "World"}


# Register resource
api.add_resource(HelloWorldResorce, '/', endpoint='hello-world', methods=['GET'])
