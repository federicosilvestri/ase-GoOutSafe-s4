from .model_test import ModelTest


class TestRestaurantAvailability(ModelTest):

    def setUp(self):
        super(TestRestaurantAvailability, self).setUp()

        from gooutsafe.models import restaurant
        from gooutsafe.models import restaurant_availability
        self.restaurant = restaurant
        self.availability = restaurant_availability

    def test_init(self):
        restaurant = self.restaurant.Restaurant('Quello Buono', 10, 20, "55555555", 'Vegetarian')
        # _avail = self.availability.RestaurantAvailability(_restaurant.__id, datetime.now(), datetime.now())
