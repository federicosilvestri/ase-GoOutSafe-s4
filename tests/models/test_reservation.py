import unittest
from datetime import datetime, timedelta

from faker import Faker

from .model_test import ModelTest


class TestReservation(ModelTest):
    faker = Faker('it_IT')

    @classmethod
    def setUpClass(cls):
        super(TestReservation, cls).setUpClass()

        from gooutsafe.models import reservation, restaurant, table, user

        cls.reservation = reservation
        cls.table = table
        cls.user = user
        cls.restaurant = restaurant

        from .test_restaurant import TestRestaurant
        cls.test_restaurant = TestRestaurant
        from .test_table import TestTable
        cls.test_table = TestTable
        from .test_user import TestUser
        cls.test_user = TestUser

    @staticmethod
    def generate_random_reservation(user=None, restaurant=None, start_time_mode=None):
        from gooutsafe.models.reservation import Reservation
        test_reservation = TestReservation()
        test_reservation.setUpClass()
        if user is None:
            user = test_reservation.test_user.generate_random_user()
        table, _ = test_reservation.test_table.generate_random_table()
        if restaurant is None:
            restaurant, _ = test_reservation.test_restaurant.generate_random_restaurant()
        people_number = test_reservation.faker.random_int(min=0,max=table.MAX_TABLE_CAPACITY)
        if start_time_mode == 'valid_past_contagion_time':
            start_time = test_reservation.faker.date_time_between_dates(datetime.utcnow()-timedelta(days=14), datetime.utcnow())
        elif start_time_mode == 'valid_future_contagion_time':
            start_time = test_reservation.faker.date_time_between('now', '+14d')
        else:
            start_time = TestReservation.faker.date_time_between('now', '+6w')
        reservation = Reservation(
            user = user,
            table = table,
            restaurant = restaurant,
            people_number = people_number,
            start_time = start_time
        )

        return reservation, (user, table, restaurant, start_time)

    @staticmethod
    def assertEqualReservations(r1, r2):
        t = unittest.FunctionTestCase(TestReservation)
        t.assertEqual(r1.user.id, r2.user.id)
        t.assertEqual(r1.table.id, r2.table.id)
        t.assertEqual(r1.restaurant.id, r2.restaurant.id)
        t.assertEqual(r1.people_number, r2.people_number)
        t.assertEqual(r1.start_time, r2.start_time)

    def test_reservation_init(self):
        reservation, (user, table, restaurant, start_time) = TestReservation.generate_random_reservation()
        self.assertEqual(reservation.user, user)
        self.assertEqual(reservation.table, table)
        self.assertEqual(reservation.start_time, start_time) 

    # def test_set_start_time(self):
    #     reservation, _ = TestReservation.generate_random_reservation()
    #     wrong_start_time = TestReservation.faker.date_time_between_dates(reservation.end_time, reservation.end_time + timedelta(weeks=10))
    #     with self.assertRaises(ValueError):
    #         reservation.set_start_time(wrong_start_time)
