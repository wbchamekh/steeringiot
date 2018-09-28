class Config(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Walid78!@localhost/steeringiot'
    STATIC_FOLDER = '/home/walid/devops/steeringiot/static/data'

class Production(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Walid78!@192.168.43.201/steeringiot'
    STATIC_FOLDER = '/home/walid/devops/steeringiot/static/data'

class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Walid78!@localhost/steeringiot'
    STATIC_FOLDER = '/home/walid/devops/steeringiot/static/data'

class TestingConfig(Config):
    TESTING = True