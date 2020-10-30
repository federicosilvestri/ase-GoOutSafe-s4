from .model_test import ModelTest
from datetime import datetime
from datetime import timedelta
from .test_restaurant import TestRestaurant
import unittest
from faker import Faker

from .model_test import ModelTest


class TestTable(ModelTest):
    faker = Faker('it_IT')

    def setUp(self):
        super(TestTable, self).setUp()

        from gooutsafe.models import table
        from gooutsafe.models import restaurant

        self.table = table
        self.restaurant = restaurant

    @staticmethod
    def generate_random_table():
        from gooutsafe.models.table import Table
        capacity = TestTable.faker.random_int(min=0,max=15)
        restaurant, _ = TestRestaurant.generate_random_restaurant()

        table = Table(capacity=capacity, restaurant=restaurant)

        return table, (capacity, restaurant)

    @staticmethod
    def assertEqualTables(t1, t2):
        t = unittest.FunctionTestCase(TestTable)
        t.assertEqual(t1.capacity, t2.capacity)
        t.assertEqual(t1.restaurant.id, t2.restaurant.id)

    def test_table_init(self):
        table, (capacity, restaurant) = TestTable.generate_random_table()
        self.assertEqual(table.capacity, capacity)
        self.assertEqual(table.restaurant.name, restaurant.name)

    def test_set_capacity(self):
        wrong_capacity = TestTable.faker.random_int()
        table, _ = TestTable.generate_random_table()
        with self.assertRaises(ValueError):
            table.set_capacity(wrong_capacity)
        
    