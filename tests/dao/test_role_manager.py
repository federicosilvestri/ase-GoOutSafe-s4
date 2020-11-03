from faker import Faker
from models.test_role import TestRole

from .dao_test import DaoTest

class TestRoleManager(DaoTest):
    faker = Faker('it_IT')

    def setUp(self):
        super(TestRoleManager, self).setUp()

        from gooutsafe.dao import role_manager
        self.role_manager = role_manager.RoleManager

    def test_create_role(self):
        role1, _ = TestRole.generate_random_role()
        self.role_manager.create_role(role=role1)
        role2 = self.role_manager.retrieve_by_id(id_=role1.id)
        TestRole.assertEqualRoles(role1,role2)

    def test_retrieve_role(self):
        role1, _ = TestRole.generate_random_role()
        self.role_manager.create_role(role=role1)
        role_name = self.role_manager.retrieve_by_name(name=role1.name)
        #tests for existing roles
        TestRole.assertEqualRoles(role1, role_name)
        #tests for non existing roles
        role_fake, _ = TestRole.generate_random_role()
        role_name = self.role_manager.retrieve_by_name(name=role_fake.name)
        self.assertIsNone(role_name, None)

    def test_delete_role(self):
        base_role, _ = TestRole.generate_random_role()
        self.role_manager.create_role(role=base_role)
        self.role_manager.delete_role(base_role)
        self.assertIsNone(self.role_manager.retrieve_by_id(base_role.id))

    def test_delete_role_by_id(self):
        base_role, _ = TestRole.generate_random_role()
        self.role_manager.create_role(role=base_role)
        self.role_manager.delete_role_by_id(base_role.id)
        self.assertIsNone(self.role_manager.retrieve_by_id(base_role.id))

    def test_delete_role_by_name(self):
        base_role, _ = TestRole.generate_random_role()
        self.role_manager.create_role(role=base_role)
        self.role_manager.delete_role_by_name(base_role.name)
        self.assertIsNone(self.role_manager.retrieve_by_id(base_role.id))