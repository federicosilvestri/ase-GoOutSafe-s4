from faker import Faker
import random
from datetime import timedelta, datetime
from models.test_table import TestTable

from .dao_test import DaoTest


class TestTableManager(DaoTest):
    faker = Faker('it_IT')

    def setUp(self):
        super(TestTableManager, self).setUp()

        from gooutsafe.dao import table_manager
        from gooutsafe.models import table

        self.table_manager = table_manager.TableManager
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