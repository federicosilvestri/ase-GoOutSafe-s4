from .model_test import ModelTest
from datetime import datetime
from datetime import timedelta
from .test_restaurant import TestRestaurant
import unittest
from faker import Faker

from .model_test import ModelTest


class TestLike(ModelTest):
    faker = Faker('it_IT')

    def setUp(self):
        super(TestLike, self).setUp()

        from gooutsafe.models import like
        from gooutsafe.models import restaurant

        self.like = like.Like
        self.restaurant = restaurant.Restaurant
