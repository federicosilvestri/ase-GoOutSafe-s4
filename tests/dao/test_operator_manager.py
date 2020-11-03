from faker import Faker
from models.test_operator import TestOperator

from .dao_test import DaoTest


class TestOperatorManager(DaoTest):
    faker = Faker('it_IT')

    def setUp(self):
        super(TestOperatorManager, self).setUp()

        from gooutsafe.dao import operator_manager
        self.operator_manager = operator_manager.OperatorManager
    
    def test_create_operator(self):
        operator1, _ = TestOperator.generate_random_operator()
        self.operator_manager.create_operator(operator=operator1)
        operator2 = self.operator_manager.retrieve_by_id(id_=operator1.id)
        TestOperator.assertOperatorsEquals(operator1, operator2)
    
    def test_delete_operator(self):
        base_operator, _ = TestOperator.generate_random_operator()
        self.operator_manager.create_operator(operator=base_operator)
        self.operator_manager.delete_operator(base_operator)
        self.assertIsNone(self.operator_manager.retrieve_by_id(base_operator.id))

    def test_delete_operator_by_id(self):
        base_operator, _ = TestOperator.generate_random_operator()
        self.operator_manager.create_operator(operator=base_operator)
        self.operator_manager.delete_operator_by_id(base_operator.id)
        self.assertIsNone(self.operator_manager.retrieve_by_id(base_operator.id))

    def test_update_operator(self):
        # @TODO: if we want to add other fields to operator
        pass