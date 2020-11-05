from faker import Faker
from flask import url_for

from tests.models.test_restaurant import TestRestaurant



from tests.views.view_test import ViewTest


class TestRestaurantView(ViewTest):
    faker = Faker('it_IT')

    def setUp(self):
        super(TestRestaurantView, self).setUp()

        from gooutsafe.dao import restaurant_manager
        self.restaurant_manager = restaurant_manager.RestaurantManager
        import gooutsafe.views.restaurants



