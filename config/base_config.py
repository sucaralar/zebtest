"""Flask config class."""
import os
import datetime


class BaseConfig:
    """Base config vars"""
    # DATABASE
    DB_HOST = os.environ.get('POSTGRES_SERVER')
    DB_NAME = os.environ.get('POSTGRES_DB')
    DB_USER = os.environ.get('POSTGRES_USER')
    DB_PWD = os.environ.get('POSTGRES_PASSWORD')
    DB_PORT = os.environ.get('POSTGRES_PORT')

    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # jwt
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=7)
