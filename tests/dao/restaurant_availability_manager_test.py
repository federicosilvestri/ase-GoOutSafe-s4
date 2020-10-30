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
<<<<<<< HEAD
                self.ram.delete_availabilitie(ava)

    def test_retrieve_by_restaurant_id(self):
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        self.re_ma.RestaurantManager.create_restaurant(restaurant)
        self.re_ma.RestaurantManager.create_restaurant(restaurant)
        start_time, end_time = TestRestaurantAvailability.generate_correct_random_times()
        ava1 = self.ava.RestaurantAvailability(restaurant.id, start_time, end_time)
        self.ram.create_availability(ava1)
        ava2 = self.ram.retrieve_by_restaurant_id(restaurant.id)
        TestRestaurantAvailability.assertEqualAvailability(ava1, ava2)
=======
                self.ram.delete_availability(ava)
>>>>>>> 7ef3385c3f26115ef3d5194b1220c0aa33b3ae9c
