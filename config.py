class Config(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Walid78!@localhost/steeringiot'

class Production(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Walid78!@192.168.43.201/steeringiot'

class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Walid78!@localhost/steeringiot'

class TestingConfig(Config):
    TESTING = True