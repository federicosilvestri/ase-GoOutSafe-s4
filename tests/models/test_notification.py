import random
import unittest

from faker import Faker
from gooutsafe.models.notification import Notification

from .model_test import ModelTest
from .test_customer import TestCustomer
from .test_operator import TestOperator
from .test_restaurant import TestRestaurant


class TestNotification(ModelTest):

    faker = Faker()

    def setUp(self):
        super(TestNotification, self).setUp()

        from gooutsafe.models import user
        self.user = user

    @staticmethod
    def generate_random_notification(user=None):
        if user is None:
            type_ = random.choice(['customer', 'operator'])
            if type_ == 'customer':
                target_user, _ = TestCustomer.generate_random_customer()
            else:
                target_user, _ = TestOperator.generator_random_operator()
        else:
            target_user = user
        positive_customer, _ = TestCustomer.generate_random_customer()
        contagion_restaurant, _ = TestRestaurant.generate_random_restaurant()
        contagion_datetime = TestNotification.faker.date_time()
        notification = Notification(target_user.id, positive_customer.id, contagion_restaurant.id, contagion_datetime)
        return notification, (target_user.id, positive_customer.id, contagion_restaurant.id, contagion_datetime)

    def test_valid_target_customer_id(self):
        customer, _ = TestCustomer.generate_random_customer()
        notification, _ = TestNotification.generate_random_notification()
        notification.set_target_user_id(customer.id)
        self.assertEqual(customer.id, notification.target_user_id)

    def test_valid_target_operator_id(self):
        operator, _ = TestOperator.generator_random_operator()
        notification, _ = TestNotification.generate_random_notification()
        notification.set_target_user_id(operator.id)
        self.assertEqual(operator.id, notification.target_user_id)

    def test_valid_positive_customer_id(self):
        customer, _ = TestCustomer.generate_random_customer()
        notification, _ = TestNotification.generate_random_notification()
        notification.set_positive_customer_id(customer.id)
        self.assertEqual(customer.id, notification.positive_customer_id)

    def test_valid_contagion_datetime(self):
        contagion_datetime, _ = self.faker.date_time()
        notification, _ = TestNotification.generate_random_notification()
        notification.set_contagion_datetime(contagion_datetime)
        self.assertEqual(contagion_datetime, notification.contagion_datetime)

    def test_valid_contagion_restaurant_id(self):
        contagion_restaurant, _ = TestRestaurant.generate_random_restaurant()
        notification, _ = TestNotification.generate_random_notification()
        notification.set_contagion_restaurant_id(contagion_restaurant)
        self.assertEqual(contagion_restaurant.id, notification.contagion_restaurant_id) 
