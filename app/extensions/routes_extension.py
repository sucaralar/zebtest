from app.api.endpoints.main import blueprint as main_roots
from app.api.endpoints.users import blueprint as users_roots
from app.api.endpoints.products import blueprint as products_roots
from app.api.endpoints.security import blueprint as security_roots


def register_routes(app):
    """
    Register routes with blueprint and namespace
    """
    app.register_blueprint(main_roots)
    app.register_blueprint(users_roots)
    app.register_blueprint(products_roots)
    app.register_blueprint(security_roots)
