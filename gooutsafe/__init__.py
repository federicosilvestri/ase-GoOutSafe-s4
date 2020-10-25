from flask import Flask

__version__ = '0.1'


def create_app(config_object):
    app = Flask(__name__, instance_relative_config=True)

    # Load config
    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)

    from .database import db, migrate
    db.init_app(app)
    migrate.init_app(app, db)

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
    import click

    @app.cli.command(short_help="Display list of URLs")
    def urls():
        print(app.url_map)
