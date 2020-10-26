import flask_login
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

__version__ = '0.1'

db = None
migrate = None
login = None


def create_app(config_object):
    global db
    global migrate
    global login

    app = Flask(__name__)
    login = flask_login.LoginManager(app)
    login.login_view = 'login'

    # Load config
    app.config.from_object(config_object)
    login_required = flask_login.login_required

    # registering db
    db = SQLAlchemy(app)

    # requiring the list of models
    import gooutsafe.models

    register_extensions(app)
    register_blueprints(app)

    # creating migrate
    migrate = Migrate(
        app=app,
        db=db
    )

    # register_cli is only called when necessary
    return app


def register_extensions(app):
    """
    It register all extensions
    :param app: Flask Application Object
    :return: None
    """

    if app.debug:
        try:
            from flask_debugtoolbar import DebugToolbarExtension
            DebugToolbarExtension(app)
        except ImportError:
            pass

    if app.testing:
        from .response import ContainsResponse
        app.response_class = ContainsResponse


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


if __name__ == '__main__':
    app = create_app('config.BaseConfig')
    register_cli(app)