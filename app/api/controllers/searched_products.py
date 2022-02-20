from flask_restx import Namespace, Resource, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.domain.manager.searched_product_manager import SearchedProductManager
from app.domain.entity.searched_product import SearchedProductBase
from app.api.serializer.searched_products import total_searched_product_serializer

ns_searched_products = Namespace('searched_products', path="/", description='Searched Products Endpoint')

searched_product_schema = ns_searched_products.schema_model(SearchedProductBase.__name__, SearchedProductBase.schema())
searched_product_model = ns_searched_products.model('GetTotalSearchedsResponse', total_searched_product_serializer)


class SearchedResource(Resource):
    """
        Endpoints for basic product crud
    """
    @jwt_required(optional=True)
    @ns_searched_products.marshal_with(searched_product_model)
    def get(self, product_id: int):
        """ Endpoint to obtain the total number of searches for a specific product """
        manager = SearchedProductManager()
        if not product_id:
            abort(404, **{"error": "You must specify a product id"})
        total = manager.get_searched(product_id=product_id)
        return {"total_searches": total}


# Register resource
ns_searched_products.add_resource(SearchedResource, '/products/<int:product_id>/total-searcheds', methods=['GET'])

