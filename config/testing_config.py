"""Flask config class."""
import os
from .base_config import BaseConfig


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True