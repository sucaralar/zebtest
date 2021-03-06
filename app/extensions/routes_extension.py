from app.api.endpoints.users import blueprint as users_roots
from app.api.endpoints.products import blueprint as products_roots
from app.api.endpoints.security import blueprint as security_roots
from app.api.endpoints.searched_products import blueprint as searched_roots


def register_routes(app):
    """
    Register routes with blueprint and namespace
    """
    app.register_blueprint(users_roots)
    app.register_blueprint(products_roots)
    app.register_blueprint(security_roots)
    app.register_blueprint(searched_roots)
