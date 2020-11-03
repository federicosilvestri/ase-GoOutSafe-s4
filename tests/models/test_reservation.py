from .model_test import ModelTest
from datetime import datetime
from datetime import timedelta
from .test_restaurant import TestRestaurant
from .test_user import TestUser
from .test_table import TestTable
import unittest

from faker import Faker

from .model_test import ModelTest


class TestReservation(ModelTest):
    faker = Faker('it_IT')

    def setUp(self):
        super(TestReservation, self).setUp()

        from gooutsafe.models import reservation
        from gooutsafe.models import table
        from gooutsafe.models import user
        from gooutsafe.models import restaurant

        self.reservation = reservation
        self.table = table
        self.user = user
        self.restaurant = restaurant

    @staticmethod
    def generate_random_reservation():
        from gooutsafe.models.reservation import Reservation
        
        user = TestUser.create_random_user()
        table, _ = TestTable.generate_random_table()
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        people_number = TestReservation.faker.random_int(min=0,max=table.MAX_TABLE_CAPACITY)
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

    def test_set_start_time(self):
        reservation, _ = TestReservation.generate_random_reservation()
        wrong_start_time = TestReservation.faker.date_time_between('-4y','now')
        with self.assertRaises(ValueError):
                reservation.set_start_time(wrong_start_time)

    def test_set_table(self):        
        reservation, _ = TestReservation.generate_random_reservation()
        table, _  = TestTable.generate_random_table()
        reservation.set_table(table)
        TestTable.assertEqualTables(table, reservation.table)

    def test_set_restaurant(self):
        reservation, _ = TestReservation.generate_random_reservation()
        restaurant, _  = TestRestaurant.generate_random_restaurant()
        reservation.set_restaurant(restaurant)
        TestRestaurant.assertEqualRestaurants(restaurant, reservation.restaurant)


    def test_set_people_number(self):
        reservation, _ = TestReservation.generate_random_reservation()
        people_number = self.faker.random_int(min=0, max=reservation.table.capacity)
        reservation.set_people_number(people_number)
        self.assertEqual(people_number, reservation.people_number)

    def test_set_end_time(self):
        reservation, _ = TestReservation.generate_random_reservation()
        wrong_endtime = self.faker.date_time_between_dates(
            datetime_start=reservation.start_time - timedelta(days=3), 
            datetime_end=reservation.start_time
            )
        with self.assertRaises(ValueError):
                reservation.set_end_time(wrong_endtime)