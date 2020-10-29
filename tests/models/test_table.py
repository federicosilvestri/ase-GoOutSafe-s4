from .model_test import ModelTest
from datetime import datetime
from datetime import timedelta
from .test_restaurant import TestRestaurant


class TestTable(ModelTest):

    def setUp(self):
        super(TestTable, self).setUp()

        from gooutsafe.models import reservation
        from gooutsafe.models import table
        from gooutsafe.models import user
        from gooutsafe.models import restaurant

        self.reservation = reservation
        self.table = table
        self.user = user
        self.restaurant = restaurant

    def test_table_init(self):
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        capacity = 3
        table = self.table.Table(3, restaurant)
        self.assertEqual(table.capacity, capacity)
        self.assertEqual(table.restaurant.name, restaurant.name)

