import os
from gooutsafe import create_app, register_cli


env = os.getenv('FLASK_ENV', 'None')
app = None

if env == 'development':
    app = create_app('config.DevConfig')
    register_cli(app)
elif env == 'testing':
    app = create_app('config.TestConfig')
else:
    raise RuntimeError("%s is not recognized as valid app environment. You have to setup the environment!" % env)

from gooutsafe import celery
