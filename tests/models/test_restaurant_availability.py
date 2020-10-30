import random
from datetime import timedelta
import unittest
from faker import Faker

from .model_test import ModelTest
from .test_restaurant import TestRestaurant


class TestRestaurantAvailability(ModelTest):
    faker = Faker()

    def setUp(self):
        super(TestRestaurantAvailability, self).setUp()

        from gooutsafe.models import restaurant
        from gooutsafe.models import restaurant_availability
        self.restaurant = restaurant
        self.availability = restaurant_availability

    @staticmethod
    def generate_correct_random_times():
        # generating times
        start_time = TestRestaurantAvailability.faker.date_time()
        end_time = start_time + timedelta(
            minutes=random.randint(10, 240)
        )

        return start_time, end_time

    @staticmethod
    def generate_bad_random_times():
        s, e = TestRestaurantAvailability.generate_correct_random_times()
        return e, s

    @staticmethod
    def generate_random_availabilities(restaurants: list, max_ava=25):
        """
        It generates, for each restaurant a set of random availabilities
        :param max_ava: maximum availabilities
        :param restaurants: a list of restaturans
        :return: a list of a list of availabilities
        """
        from gooutsafe.models.restaurant_availability import RestaurantAvailability

        rest_ava = []
        for rest in restaurants:
            avas = []
            for _ in range(0, random.randint(1, max_ava)):
                s, e = TestRestaurantAvailability.generate_correct_random_times()
                ava = RestaurantAvailability(
                    rest.id,
                    s,
                    e
                )
                avas.append(ava)
            rest_ava.append(avas)

        return rest_ava

    @staticmethod
    def assertEqualAvailability(ra1, ra2):
        t = unittest.FunctionTestCase(TestRestaurantAvailability)
        t.assertEqual(ra1.start_time, ra2.start_time)
        t.assertEqual(ra1.end_time, ra2.end_time)
        t.assertEqual(ra1.restaurant.id, ra2.restaurant.id)

    def test_init(self):
        for _ in range(0, 10):
            restaurant, _ = TestRestaurant.generate_random_restaurant()
            start_time, end_time = self.generate_correct_random_times()
            _avail = self.availability.RestaurantAvailability(
                restaurant.id,
                start_time,
                end_time
            )

            self.assertEqual(start_time, _avail.start_time)
            self.assertEqual(end_time, _avail.end_time)

            with self.assertRaises(ValueError):
                _avail = self.availability.RestaurantAvailability(
                    restaurant.id,
                    end_time,
                    start_time
                )

    def test_set_times(self):
        for _ in range(0, 10):
            restaurant, _ = TestRestaurant.generate_random_restaurant()
            start_time, end_time = self.generate_correct_random_times()
            _avail = self.availability.RestaurantAvailability(
                restaurant.id,
                start_time,
                end_time
            )
            _avail.set_times(start_time, end_time)

            self.assertEqual(start_time, _avail.start_time)
            self.assertEqual(end_time, _avail.end_time)

            with self.assertRaises(ValueError):
                _avail.set_times(
                    end_time,
                    start_time
                )
