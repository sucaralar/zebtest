from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_current_user
from app.domain.entity import ProductBase

api = Namespace('products', path="/products/", description='Products Endpoint')


class ProductResource(Resource):
    @jwt_required(optional=True)
    def get(self, product_id: int = None):
        """ Endpoint to get a product(s) """
        if product_id:
            # check if is an anonymous user
            user = get_current_user()
            if not user:
                pass
            response = {}

        else:
            response = []
        return response

    @jwt_required()
    def post(self, product_in: ProductBase):
        """ Create new product """
        return {}

    @jwt_required()
    def put(self, product_in: ProductBase):
        """ Update and existent product """
        return {}

    @jwt_required()
    def delete(self, product_id: int):
        """ Delete and existent product """
        return {}


# Register resource
api.add_resource(ProductResource, '/', endpoint='products-list', methods=['GET'])
api.add_resource(ProductResource, '/<int:product_id>', endpoint='products-get', methods=['GET'])
api.add_resource(ProductResource, '/', endpoint='products-update', methods=['PUT'])
api.add_resource(ProductResource, '/', endpoint='products-delete', methods=['DELETE'])
