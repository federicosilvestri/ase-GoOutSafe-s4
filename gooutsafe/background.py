from celery import Celery

from gooutsafe import db

BACKEND = BROKER = 'redis://localhost:6379'
celery = Celery(__name__, backend=BACKEND, broker=BROKER)

_APP = None


@celery.task
def do_task():
    global _APP
    # lazy init
    if _APP is None:
        from gooutsafe.initial_data import create_app
        app = create_app()
        db.init_app(app)
    else:
        app = _APP

    return []
