from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.domain.manager import ProductManager
from app.domain.entity.products import ProductBase
from app.api.serializer.products import product_serializer

api = Namespace('products', path="/products/", description='Products Endpoint')

product_schema = api.schema_model(ProductBase.__name__, ProductBase.schema())
product_model = api.model('ProductModel', product_serializer)


class ProductResource(Resource):
    @jwt_required(optional=True)
    # @api.marshal_with(product_model)
    def get(self, product_id: int = None):
        """ Endpoint to get a product(s) """
        manager = ProductManager()
        if product_id:
            response = manager.get_by_id(product_id=product_id)
            # check if is an anonymous user
            user = get_jwt_identity()
            if not user:
                pass
        else:
            response = manager.get_list()
        return response

    @jwt_required()
    @api.marshal_with(product_model)
    @api.expect(product_schema)
    def post(self):
        """ Create new product """
        manager = ProductManager()
        product_in = ProductBase(**api.payload)
        response = manager.create(product_in=product_in)
        return response

    @jwt_required()
    @api.marshal_with(product_model)
    @api.expect(product_schema)
    def put(self):
        """ Update update a existent product """
        manager = ProductManager()
        product_in = ProductBase(**api.payload)
        response = manager.update(product_in=product_in)
        return response

    @jwt_required()
    def delete(self, product_id: int):
        """ Delete update a existent product """
        manager = ProductManager()
        response = manager.delete(product_id=product_id)
        return {"deleted": response}


# Register resource
api.add_resource(ProductResource, '/', endpoint='products-list', methods=['GET'])
api.add_resource(ProductResource, '/<int:product_id>', endpoint='products-get', methods=['GET'])
api.add_resource(ProductResource, '/', endpoint='products-create', methods=['POST'])
api.add_resource(ProductResource, '/', endpoint='products-update', methods=['PUT'])
api.add_resource(ProductResource, '/<int:product_id>', endpoint='products-delete', methods=['DELETE'])
