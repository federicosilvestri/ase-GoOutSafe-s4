class BaseConfig(object):
    """
    This is the main configuration object for application.
    """
    DEBUG = True

    # import os; os.urandom(24)
    # To set up in instance.py
    SECRET_KEY = b'isreallynotsecretatall'

    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestConfig(object):
    """
    This is the main configuration object for application.
    """
    DEBUG = True

    # import os; os.urandom(24)
    # To set up in instance.py
    SECRET_KEY = b'isreallynotsecretatall'

    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db_test.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
