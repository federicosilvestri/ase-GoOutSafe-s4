import unittest

from .view_test import ViewTest


class TestReviewViews(ViewTest):

    @classmethod
    def setUpClass(cls):
        super(TestReviewViews, cls).setUpClass()
        from gooutsafe.dao.restaurant_manager import RestaurantManager
        cls.restaurant_manager = RestaurantManager
        from tests.models.test_restaurant import TestRestaurant
        cls.test_restaurant = TestRestaurant 
        from tests.models.test_restaurant_availability import TestRestaurantAvailability
        cls.test_availability = TestRestaurantAvailability

    def test_write_review_get(self):
        pass