from datetime import datetime, timedelta

from gooutsafe import celery
from gooutsafe.dao.customer_manager import CustomerManager

# @celery.on_after_finalize.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(5.0, revert_customer_health_status.s(), name='once_after_14_days')

def schedule_revert_customer_health_status(customer, eta=None):
    if not eta:
        eta = datetime.utcnow() + timedelta(days=14)
    customer_id = customer.id
    revert_customer_health_status.apply_async(customer_id, eta=eta)

@celery.task
def revert_customer_health_status(customer_id):
    customer = CustomerManager.retrieve_by_id(customer_id)
    if customer:
        customer.set_health_status(False)
        CustomerManager.update_customer(customer=customer)
