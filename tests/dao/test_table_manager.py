import random
from datetime import datetime, timedelta

from faker import Faker
from models.test_restaurant import TestRestaurant
from models.test_table import TestTable

from .dao_test import DaoTest


class TestTableManager(DaoTest):
    faker = Faker('it_IT')

    def setUp(self):
        super(TestTableManager, self).setUp()

        from gooutsafe.dao import table_manager
        from gooutsafe.models import table

        self.table_manager = table_manager.TableManager
        from gooutsafe.dao import restaurant_manager
        self.restaurant_manager = restaurant_manager.RestaurantManager
        self.table = table
    
    def test_create_table(self):
        table1, _ = TestTable.generate_random_table()
        self.table_manager.create_table(table=table1)
        table2 = self.table_manager.retrieve_by_id(id_=table1.id)
        TestTable.assertEqualTables(table1, table2)

    def test_delete_table(self):
        base_table, _ = TestTable.generate_random_table()
        self.table_manager.create_table(table=base_table)
        self.table_manager.delete_table(base_table)
        self.assertIsNone(self.table_manager.retrieve_by_id(base_table.id))

    def test_delete_table_by_id(self):
        base_table, _ = TestTable.generate_random_table()
        self.table_manager.create_table(table=base_table)
        self.table_manager.delete_table_by_id(base_table.id)
        self.assertIsNone(self.table_manager.retrieve_by_id(base_table.id))

    def test_update_table(self):
        base_table, _ = TestTable.generate_random_table()
        self.table_manager.create_table(table=base_table)
        base_table.set_capacity(random.randint(self.table.Table.MIN_TABLE_CAPACITY, self.table.Table.MAX_TABLE_CAPACITY))
        updated_table = self.table_manager.retrieve_by_id(id_=base_table.id)
        TestTable.assertEqualTables(base_table, updated_table)
    
    def test_multiple_tables_retrieved_by_restaurant_id(self):
        base_tables = []
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        for _ in range(random.randint(2, 10)):
            table, _ = TestTable.generate_random_table()
            base_tables.append(table)
            table.restaurant = restaurant
        self.restaurant_manager.create_restaurant(restaurant=restaurant)
        for table in base_tables:
            self.table_manager.create_table(table=table)
        retrieved_tables = self.table_manager.retrieve_by_restaurant_id(restaurant_id=restaurant.id)
        for base_table, retrieved_table in zip(base_tables, retrieved_tables):
            TestTable.assertEqualTables(base_table, retrieved_table)
