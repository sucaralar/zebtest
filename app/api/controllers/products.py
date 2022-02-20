from flask_restx import Namespace, Resource, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.domain.manager.product_manager import ProductManager
from app.domain.entity.products import ProductBase
from app.api.serializer.products import product_serializer

ns_products = Namespace('products', path="/", description='Products Endpoint')

product_schema = ns_products.schema_model(ProductBase.__name__, ProductBase.schema())
product_model = ns_products.model('ProductResponse', product_serializer)


class ProductResource(Resource):
    """
        Endpoints for basic product crud
    """
    @jwt_required(optional=True)
    @ns_products.marshal_with(product_model)
    def get(self, product_id: int = None):
        """ Endpoint to get a product(s) """
        manager = ProductManager()
        if product_id:
            user = get_jwt_identity()
            response = manager.get_by_id(product_id=product_id, user=user)
            if not response:
                abort(404, **{"error": "There is no product with the specified ID"})
        else:
            response = manager.get_list()
        return response

    @jwt_required()
    @ns_products.marshal_with(product_model)
    @ns_products.expect(product_schema)
    def post(self):
        """ Create new product """
        manager = ProductManager()
        product_in = ProductBase(**ns_products.payload)
        response = manager.create(product_in=product_in)
        return response

    @jwt_required()
    @ns_products.marshal_with(product_model)
    @ns_products.expect(product_schema)
    def put(self):
        """ Update update a existent product """
        manager = ProductManager()
        product_in = ProductBase(**ns_products.payload)
        response = manager.update(product_in=product_in)
        return response

    @jwt_required()
    def delete(self, product_id: int):
        """ Delete update a existent product """
        manager = ProductManager()
        response = manager.delete(product_id=product_id)
        return {"deleted": response}


# Register resource
ns_products.add_resource(ProductResource, '/products', methods=['GET', 'POST', 'PUT'])
ns_products.add_resource(ProductResource, '/products/<int:product_id>', methods=['GET', 'DELETE'])
