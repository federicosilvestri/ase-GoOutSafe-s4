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
            role, name = TestRole.generate_random_role()
            self.assertEqual(role.name, name)

    @staticmethod
    def assertEqualRoles(r1, r2):
        r = unittest.FunctionTestCase(TestRole)
        r.assertEqual(r1.name, r2.name)

    @staticmethod
    def generate_random_role():
        from gooutsafe.models import Role

        role_name = TestRole.faker.job()
        role = Role(name=role_name)

        return role, role_name