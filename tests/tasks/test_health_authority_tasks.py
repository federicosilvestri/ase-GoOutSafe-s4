from random import randint

from unittest.mock import patch

from models.test_authority import TestAuthority
from models.test_customer import TestCustomer
from models.test_operator import TestOperator
from models.test_restaurant import TestRestaurant
from models.test_reservation import TestReservation

from .tasks_test import TasksTest


class TestHealthAuthorityTasks(TasksTest):

    def setUp(self):
        super(TestHealthAuthorityTasks, self).setUp()

        from gooutsafe.dao import health_authority_manager
        self.health_authority_manager = health_authority_manager.AuthorityManager
        from gooutsafe.dao import customer_manager
        self.customer_manager = customer_manager.CustomerManager
        from gooutsafe.dao import operator_manager
        self.operator_manager = operator_manager.OperatorManager
        from gooutsafe.dao import restaurant_manager
        self.restaurant_manager = restaurant_manager.RestaurantManager
        from gooutsafe.dao import reservation_manager
        self.reservation_manager = reservation_manager.ReservationManager
        from gooutsafe.dao import notification_manager
        self.notification_manager = notification_manager.NotificationManager

        from gooutsafe.tasks import health_authority_tasks
        self.health_authority_tasks = health_authority_tasks


    # def test_schedule_revert_health_status(self):
    #     with patch('gooutsafe.tasks.health_authority_tasks.revert_customer_health_status') as task_mock:
    #         customer, _ = TestCustomer.generate_random_customer()
    #         self.customer_manager.create_customer(customer=customer)
    #         self.health_authority_tasks.schedule_revert_customer_health_status(customer)
    #         assert task_mock.called

    def test_revert_health_status(self):
        # authority, _ = TestAuthority.generate_random_authority()
        # self.health_authority_manager.create_authority(authority=authority)
        customer, _ = TestCustomer.generate_random_customer()
        customer.set_health_status(True)
        self.customer_manager.create_customer(customer=customer)
        customer_id = customer.id
        self.health_authority_tasks.revert_customer_health_status(customer.id)
        customer_retrieved = self.customer_manager.retrieve_by_id(customer_id)
        self.assertEqual(customer_retrieved.health_status, False)

    def test_notify_restaurant_owners_about_positive_past_customer(self):
        # create positive customer
        customer, _ = TestCustomer.generate_random_customer()
        customer.set_health_status(True)
        self.customer_manager.create_customer(customer=customer)
        customer_id = customer.id
        notifications_data = []
        for _ in range(randint(2, 10)):
            # create random owners
            operator, _ = TestOperator.generate_random_operator()
            # create random restaurant for each owner
            restaurant, _ = TestRestaurant.generate_random_restaurant()
            self.operator_manager.create_operator(operator=operator)
            restaurant.owner_id = operator.id
            self.restaurant_manager.create_restaurant(restaurant=restaurant)
            # create random reservation for customer in each restaurant
            reservation, _ = TestReservation.generate_random_reservation(user=customer, restaurant=restaurant, start_time_mode='valid_past_contagion_time')
            self.reservation_manager.create_reservation(reservation=reservation)
            notifications_data.append((operator.id, restaurant.id, reservation.id))
        self.health_authority_tasks.notify_restaurant_owners_about_positive_past_customer(customer)
        # check if notifications are there
        customer = self.customer_manager.retrieve_by_id(customer_id)
        for operator_id, restaurant_id, reservation_id in notifications_data:
            operator = self.operator_manager.retrieve_by_id(operator_id)
            restaurant = self.restaurant_manager.retrieve_by_id(restaurant_id)
            reservation = self.reservation_manager.retrieve_by_id(reservation_id)
            notification = self.notification_manager.retrieve_by_target_user_id(operator.id)[0]
            self.assertEqual(notification.target_user_id, operator.id)
            self.assertEqual(notification.positive_customer_id, customer.id)
            self.assertEqual(notification.contagion_restaurant_id, restaurant.id)
            self.assertEqual(notification.contagion_datetime, reservation.start_time)
