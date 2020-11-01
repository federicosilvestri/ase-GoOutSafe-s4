from faker import Faker
from .dao_test import DaoTest
from tests.models.test_restaurant import TestRestaurant
from tests.models.test_restaurant_availability import TestRestaurantAvailability


class RestaurantAvailabilityManager(DaoTest):
    faker = Faker()

    def setUp(self):
        super(RestaurantAvailabilityManager, self).setUp()

        from gooutsafe.dao import restaurant_availability_manager
        from gooutsafe.dao import restaurant_manager
        from gooutsafe.models import restaurant_availability
        self.ram = restaurant_availability_manager.RestaurantAvailabilityManager
        self.ava = restaurant_availability
        self.re_ma = restaurant_manager

    def test_crud(self):
        rests = []
        for _ in range(0, 10):
            restaurant, _ = TestRestaurant.generate_random_restaurant()
            self.re_ma.RestaurantManager.create_restaurant(restaurant)
            rests.append(restaurant)

        rests_ava = TestRestaurantAvailability.generate_random_availabilities(
            rests
        )

        # test create
        for avas in rests_ava:
            for ava in avas:
                self.ram.create_availability(ava)

        # test update
        for avas in rests_ava:
            for ava in avas:
                s, e = TestRestaurantAvailability.generate_correct_random_times()
                ava.set_times(s, e)
                self.ram.update_availability(ava)

        # test update
        for avas in rests_ava:
            for ava in avas:
                self.ram.delete_availability(ava)
