import os

import flask_login
from celery import Celery
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker
from flask_environments import Environments
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

__version__ = '0.1'

db = None
migrate = None
login = None
debug_toolbar = None
app = None
celery = None

def create_app(config_object, new_one=False):
    global db
    global app
    global migrate
    global login
    global celery

    if not new_one and app is not None:
        return app

    app = Flask(__name__, instance_relative_config=True)

    # Load config
    env = Environments(app)
    env.from_object(config_object)

    login = flask_login.LoginManager(app)
    login.login_view = 'auth.login'

    # registering db
    db = SQLAlchemy(
        app=app
    )

    # creating celery
    celery = make_celery(app)

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
    if os.getenv('FLASK_ENV') == 'testing':
        # we need to populate the db
        db.create_all()

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

    if app.testing:
        from .response import ContainsResponse
        app.response_class = ContainsResponse

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


def make_celery(app):
    BACKEND = BROKER = 'redis://localhost:6379'
    celery = Celery(
        app.name,
        broker=BROKER,
        backend=BACKEND
    )
    celery.conf.timezone = 'Europe/Rome'
    celery.conf.update(app.config)
    celery.conf.imports = ('gooutsafe.tasks.home_tasks',)
    # celery.conf.beat_schedule = {
    #     "every-5-seconds": {
    #         "task": "gooutsafe.tasks.home_tasks.ciao",
    #         "schedule": 10.0
    #     }
    # }

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
