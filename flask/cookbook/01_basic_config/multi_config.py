class BaseConfig:
    SECRET_KEY = 'abc123'
    DEBUG = True
    TESTING = False
    NEW_CONFIG_VARAIBLE = 'my value'


class ProdConfig(BaseConfig):
    DEBUG = False
    SECRET_KEY = '12345'


class StagingConfig(BaseConfig):
    DEBUG = True


class DevConfig(BaseConfig):
    TESTING = True
    SECRET_KEY = '890xyz'
    
