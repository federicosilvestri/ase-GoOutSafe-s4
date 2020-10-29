from faker import Faker
from models.test_user import TestUser

from .dao_test import DaoTest


class TestUserManager(DaoTest):
    faker = Faker()

    def setUp(self):
        super(TestUserManager, self).setUp()

        from gooutsafe.dao import user_manager

        self.user_manager = user_manager.UserManager

    def test_crud(self):
        for _ in range(0, 10):
            user = TestUser.create_random_user()
            self.user_manager.create_user(user=user)
            user1 = self.user_manager.retrieve_by_id(user.id)
            TestUser.assertUserEquals(user1, user)

            user.set_password(self.faker.password())
            user.email = self.faker.email()
            self.user_manager.update_user(user=user)
            user1 = self.user_manager.retrieve_by_id(user.id)
            TestUser.assertUserEquals(user1, user)

            self.user_manager.delete_user(user=user)







