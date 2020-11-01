import flask_login
from flask import Flask
import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_environments import Environments
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker

__version__ = '0.1'

db = None
migrate = None
login = None
debug_toolbar = None


def create_app():
    global db
    global app
    global migrate
    global login

    app = Flask(__name__, instance_relative_config=True)

    flask_env = os.getenv('FLASK_ENV', 'None')
    if flask_env == 'development':
        config_object = 'config.DevConfig'
        register_cli(app)
    elif flask_env == 'testing':
        config_object = 'config.TestConfig'
    else:
        raise RuntimeError("%s is not recognized as valid app environment. You have to setup the environment!" % env)

    # Load config
    env = Environments(app)
    env.from_object(config_object)

    login = flask_login.LoginManager(app)
    login.login_view = 'auth.login'

    # registering db
    db = SQLAlchemy(
        app=app
    )

    # requiring the list of models
    import gooutsafe.models

    register_extensions(app)
    register_blueprints(app)

    # creating migrate
    migrate = Migrate(
        app=app,
        db=db
    )

    # checking the environment
    if flask_env == 'testing':
        # we need to populate the db
        db.create_all()
        print("CREATING SB")
    elif flask_env == 'development':
        register_cli(app)

    return app


def register_extensions(app):
    """
    It register all extensions
    :param app: Flask Application Object
    :return: None
    """
    global debug_toolbar

    if app.debug:
        try:
            from flask_debugtoolbar import DebugToolbarExtension
            debug_toolbar = DebugToolbarExtension(app)
        except ImportError:
            pass

    # adding bootstrap and date picker
    Bootstrap(app)
    datepicker(app)


def register_blueprints(app):
    """
    This function registers all views in the flask application
    :param app: Flask Application Object
    :return: None
    """
    from gooutsafe.views import blueprints
    for bp in blueprints:
        app.register_blueprint(bp, url_prefix='/')


def register_cli(app):
    @app.cli.command(short_help="Display list of URLs")
    def urls():
        print(app.url_map)
