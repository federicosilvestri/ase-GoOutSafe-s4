from .model_test import ModelTest
import random
from faker import Faker


class TestUser(ModelTest):

    faker = Faker()

    def setUp(self):
        super(TestUser, self).setUp()

        from gooutsafe.models import user
        self.user = user

    @staticmethod
    def assertUserEquals(value, expected):
        t = TestUser()
        t.assertEqual(value.email, expected.email)
        t.assertEqual(value.password, expected.password)
        t.assertEqual(value.is_active, expected.is_active)
        t.assertEqual(value.authenticated, False)
        t.assertEqual(value.is_anonymous, expected.is_anonymous)

    @staticmethod
    def create_random_user():
        email = TestUser.faker.email()
        password = TestUser.faker.password()
        is_active = TestUser.faker.boolean()
        is_admin = TestUser.faker.boolean()
        authenticated = TestUser.faker.boolean()
        is_anonymous = TestUser.faker.boolean()
        type_ = random.choice(['customer, operator, health_authority'])

        from gooutsafe.models import User

        user = User(
            email=email,
            password=password,
            is_active=is_active,
            is_admin=is_admin,
            authenticated=authenticated,
            is_anonymous=is_anonymous,
            type=type_
        )

        return user
