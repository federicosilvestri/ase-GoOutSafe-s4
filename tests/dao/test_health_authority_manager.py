from faker import Faker

from .dao_test import DaoTest
from tests.models.test_authority import TestAuthority


class TestAuthorityManager(DaoTest):
    faker = Faker()

    def setUp(self):
        super(TestAuthorityManager, self).setUp()

        from gooutsafe.dao import health_authority_manager

        self.health_authority_manager = health_authority_manager.AuthorityManager

    def test_crud(self):
        for _ in range(0, 10):
            authority, _ = TestAuthority.generate_random_authority()
            self.health_authority_manager.create_authority(authority=authority)
            authority1 = self.health_authority_manager.retrieve_by_id(authority.id)
            TestAuthority.assertAuthorityEquals(authority1, authority)