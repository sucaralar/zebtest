from .prod_config import ProductionConfig
from .dev_config import DevelopmentConfig
from .testing_config import TestingConfig

configurations = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig, 
    'default': DevelopmentConfig
}
