import random
import unittest

from faker import Faker

from .model_test import ModelTest
from .test_customer import TestCustomer
from .test_operator import TestOperator
from .test_restaurant import TestRestaurant


class TestNotification(ModelTest):

    faker = Faker()

    def setUp(self):
        super(TestNotification, self).setUp()

    @staticmethod
    def generate_random_notification(target_user=None):
        from gooutsafe.models import notification
        if target_user is None:
            type_ = random.choice(['customer', 'operator'])
            if type_ == 'customer':
                target_user, _ = TestCustomer.generate_random_customer()
            else:
                target_user, _ = TestOperator.generator_random_operator()
        positive_customer, _ = TestCustomer.generate_random_customer()
        contagion_restaurant, _ = TestRestaurant.generate_random_restaurant()
        contagion_datetime = TestNotification.faker.date_time()
        notification = notification.Notification(target_user.id, positive_customer.id, contagion_restaurant.id, contagion_datetime)
        return notification, (target_user.id, positive_customer.id, contagion_restaurant.id, contagion_datetime)

    @staticmethod
    def assertEqualNotifications(n1, n2):
        t = unittest.FunctionTestCase(TestNotification)
        t.assertEqual(n1.target_user_id, n2.target_user_id)
        t.assertEqual(n1.positive_customer_id, n2.positive_customer_id)
        t.assertEqual(n1.contagion_restaurant_id, n2.contagion_restaurant_id)
        t.assertEqual(n1.contagion_datetime, n2.contagion_datetime)
        t.assertEqual(n1.timestamp, n2.timestamp)

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
        contagion_datetime = self.faker.date_time()
        notification, _ = TestNotification.generate_random_notification()
        notification.set_contagion_datetime(contagion_datetime)
        self.assertEqual(contagion_datetime, notification.contagion_datetime)

    def test_valid_contagion_restaurant_id(self):
        contagion_restaurant, _ = TestRestaurant.generate_random_restaurant()
        notification, _ = TestNotification.generate_random_notification()
        notification.set_contagion_restaurant_id(contagion_restaurant.id)
        self.assertEqual(contagion_restaurant.id, notification.contagion_restaurant_id) 
