import os

from celery import Celery
from flask import Flask, render_template
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
celery = None


def create_app():
    global db
    global app
    global migrate
    global login
    global celery

    app = Flask(__name__, instance_relative_config=True)
    app.register_error_handler(404, page_not_found)

    flask_env = os.getenv('FLASK_ENV', 'None')
    if flask_env == 'development':
        config_object = 'config.DevConfig'
    elif flask_env == 'testing':
        config_object = 'config.TestConfig'
    else:
        raise RuntimeError("%s is not recognized as valid app environment. You have to setup the environment!" % flask_env)

    # Load config
    env = Environments(app)
    env.from_object(config_object)

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

    # loading login manager
    import gooutsafe.auth as auth
    login = auth.init_login_manager(app)

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


def make_celery(app):
    BACKEND = BROKER = 'redis://localhost:6379'
    celery = Celery(
        app.name,
        broker=BROKER,
        backend=BACKEND
    )
    celery.conf.timezone = 'Europe/Rome'
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

def page_not_found(e):
  return render_template('404.html'), 404