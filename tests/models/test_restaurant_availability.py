from .model_test import ModelTest
from .test_restaurant import  TestRestaurant



class TestRestaurantAvailability(ModelTest):

    def setUp(self):
        super(TestRestaurantAvailability, self).setUp()

        from gooutsafe.models import restaurant
        from gooutsafe.models import restaurant_availability
        self.restaurant = restaurant
        self.availability = restaurant_availability

    def test_init(self):
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        # _avail = self.availability.RestaurantAvailability(_restaurant.__id, datetime.now(), datetime.now())
