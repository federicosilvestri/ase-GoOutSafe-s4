from .model_test import ModelTest
from datetime import datetime
from datetime import timedelta


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
        restaurant = self.restaurant.Restaurant('Quello Buono', 10, 20, "55555555", 'Vegetarian')
        capacity = 3
        table = self.table.Table(3, restaurant)
        self.assertEqual(table.capacity, capacity)
        self.assertEqual(table.restaurant.name, restaurant.name)

