import unittest

from faker import Faker

from .model_test import ModelTest

class TestRole(ModelTest):

    faker = Faker('it_IT')

    def setUp(self):
        super(TestRole, self).setUp()
        from gooutsafe.models import role
        self.role = role

    def test_role_init(self):
        for _ in range(0,10):
            pass

    @staticmethod
    def generate_random_role():
        pass