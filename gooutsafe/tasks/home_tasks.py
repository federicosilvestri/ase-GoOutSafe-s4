from gooutsafe import celery

@celery.task(name='gooutsafe.tasks.delay')
def print_with_delay():
    print('PER FAVORE')
    
@celery.task
def ciao():
    print('ciao')
