class Config(object):
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    """
    This is the main configuration object for application.
    """
    DEBUG = True
    TESTING = True

    SECRET_KEY = b'isreallynotsecretatall'

    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestConfig(DevConfig):
    """
    This is the main configuration object for application.
    """
    TESTING = True

    import os
    SECRET_KEY = os.urandom(24)

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
