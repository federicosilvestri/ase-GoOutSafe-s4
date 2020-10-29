import random
import string

from faker import Faker

from .dao_test import DaoTest
from tests.models.test_user import TestUser


class TestUserManager(DaoTest):
    faker = Faker()

    def setUp(self):
        super(TestUserManager, self).setUp()

        from gooutsafe.dao import user_manager

        self.user_manager = user_manager.UserManager

    def test_create(self):
        user = TestUser.create_random_user()

        self.user_manager.create(user=user)
        user1 = self.user_manager.retrieve(user.id)

        TestUser.assertUserEquals(user1, user)




