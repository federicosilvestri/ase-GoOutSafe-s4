from .model_test import ModelTest


class TestRestaurantRating(ModelTest):

    def setUp(self):
        super(TestRestaurantRating, self).setUp()

        from gooutsafe.models import restaurant_rating
        from gooutsafe.models import customer
        from gooutsafe.models import restaurant

        self.restaurant_rating = restaurant_rating
        self.customer = customer
        self.restaurant = restaurant

    def test_init(self):
        restaurant = self.restaurant.Restaurant(
            'Quello Buono',
            10,
            20,
            "55555555",
            'Vegetarian'
        )

        from .test_customer import TestCustomer
        customer = TestCustomer.generate_random_customer()


