from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from config import configurations

db = SQLAlchemy()
jwt_manager = JWTManager()
api = Api(doc='/',
          title='Zebrans Test - Resource API',
          version='1.0',
          description='This is the api documentation created by Susana Carrillo for the Zebrans team')


def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(configurations[environment])
    db.init_app(app)
    api.init_app(app)
    from app.extensions.routes_extension import register_routes
    register_routes(app)
    jwt_manager.init_app(app)
    return app
