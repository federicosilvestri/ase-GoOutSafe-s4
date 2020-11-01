from gooutsafe import celery

@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(5.0, print_with_delay.s(), name='add_every_10')
    sender.add_periodic_task(7.0, ciao.s(), expires=10)


@celery.task()
def print_with_delay():
    print('PER FAVORE')


@celery.task
def ciao():
    print('ciao')
