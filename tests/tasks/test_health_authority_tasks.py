from models.test_customer import TestCustomer
from models.test_authority import TestAuthority

from .tasks_test import TasksTest


class TestHealthAuthorityTasks(TasksTest):

    def setUp(self):
        super(TestHealthAuthorityTasks, self).setUp()

        from gooutsafe.dao import health_authority_manager
        self.health_authority_manager = health_authority_manager.AuthorityManager
        from gooutsafe.dao import customer_manager
        self.customer_manager = customer_manager.CustomerManager
        from gooutsafe.tasks import health_authority_tasks
        self.health_authority_tasks = health_authority_tasks

    def test_revert_health_status(self):
        # authority, _ = TestAuthority.generate_random_authority()
        # self.health_authority_manager.create_authority(authority=authority)
        customer, _ = TestCustomer.generate_random_customer()
        customer.set_health_status(True)
        self.customer_manager.create_customer(customer=customer)
        self.health_authority_tasks.revert_customer_health_status(customer.id)
        self.assertEqual(customer.health_status, False)
