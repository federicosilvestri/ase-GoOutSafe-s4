from datetime import datetime, timedelta

from gooutsafe import celery
from gooutsafe.dao.customer_manager import CustomerManager
from gooutsafe.dao.notification_manager import NotificationManager
from gooutsafe.dao.reservation_manager import ReservationManager
from gooutsafe.models.notification import Notification


def schedule_revert_customer_health_status(customer, eta=None):
    if not eta:
        eta = datetime.utcnow() + timedelta(days=14)
    customer_id = customer.id
    revert_customer_health_status.apply_async(kwargs={"customer_id": customer_id}, eta=eta)


@celery.task
def revert_customer_health_status(customer_id):
    customer = CustomerManager.retrieve_by_id(customer_id)
    if customer:
        customer.set_health_status(False)
        CustomerManager.update_customer(customer=customer)
    else:
        raise ValueError('Customer does not exist anymore')


@celery.task
def notify_restaurant_owners_about_positive_past_customer(customer):
    reservations = ReservationManager.retrieve_by_customer_id_in_last_14_days(customer.id)
    for reservation in reservations:
        restaurant = reservation.restaurant
        owner = restaurant.owner
        notification = Notification(owner.id, customer.id, restaurant.id, reservation.start_time)
        NotificationManager.create_notification(notification=notification)
