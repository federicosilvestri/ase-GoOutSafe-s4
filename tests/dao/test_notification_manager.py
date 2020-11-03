from datetime import datetime, timedelta

from faker import Faker
from models.test_customer import TestCustomer
from models.test_notification import TestNotification
from models.test_reservation import TestReservation
from models.test_restaurant import TestRestaurant
from models.test_table import TestTable
from models.test_user import TestUser

from .dao_test import DaoTest


class TestNotificationManager(DaoTest):
    faker = Faker('it_IT')

    def setUp(self):
        super(TestNotificationManager, self).setUp()

        from gooutsafe.dao import reservation_manager
        self.reservation_manager = reservation_manager.ReservationManager
        from gooutsafe.dao import customer_manager
        self.customer_manager = customer_manager.CustomerManager
        from gooutsafe.dao import user_manager
        self.user_manager = user_manager.UserManager
        from gooutsafe.dao import restaurant_manager
        self.restaurant_manager = restaurant_manager.RestaurantManager
        from gooutsafe.dao import customer_manager
        self.customer_manager = customer_manager.CustomerManager

        from gooutsafe.dao import user_manager
        self.user_manager = user_manager.UserManager
        from gooutsafe.dao import notification_manager
        self.notification_manager = notification_manager.NotificationManager

    def test_create_notification(self):
        notification, _ = TestNotification.generate_random_notification()
        self.notification_manager.create_notification(notification=notification)
        retrieved_notification = self.notification_manager.retrieve_by_id(id_=notification.id)
        TestNotification.assertEqualNotifications(notification, retrieved_notification)

    def test_update_notification(self):
        notification, _ = TestNotification.generate_random_notification()
        self.notification_manager.create_notification(notification=notification)
        notification.set_contagion_datetime(TestNotificationManager.faker.date_time())
        self.notification_manager.update_notification(notification=notification)
        retrieved_notification = self.notification_manager.retrieve_by_id(id_=notification.id)
        TestNotification.assertEqualNotifications(notification, retrieved_notification)

    def test_delete_notification(self):
        notification, _ = TestNotification.generate_random_notification()
        self.notification_manager.create_notification(notification=notification)
        self.notification_manager.delete_notification(notification=notification)
        self.assertIsNone(self.notification_manager.retrieve_by_id(id_=notification.id))

    def test_delete_notification_by_id(self):
        notification, _ = TestNotification.generate_random_notification()
        self.notification_manager.create_notification(notification=notification)
        self.notification_manager.delete_notification_by_id(id_=notification.id)
        self.assertIsNone(self.notification_manager.retrieve_by_id(id_=notification.id))
    
    def test_retrieve_notification_by_target_user_id(self):
        target_user = TestUser.generate_random_user()
        self.user_manager.create_user(user=target_user)
        notification, _ = TestNotification.generate_random_notification(target_user)
        self.notification_manager.create_notification(notification=notification)
        retrieved_notification = self.notification_manager.retrieve_by_target_user_id(user_id=target_user.id)[0]
        TestNotification.assertEqualNotifications(notification, retrieved_notification)
