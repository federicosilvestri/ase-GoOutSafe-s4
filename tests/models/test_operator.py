from .model_test import ModelTest


class TestOperator(ModelTest):

    def setUp(self):
        super(TestOperator, self).setUp()

        from gooutsafe.models import operator
        self.operator = operator

    def test_cust_init(self):
        for i in range(0, 10):
            random_operator = TestOperator.generator_random_operator()
            operator, (email, password, is_active, is_admin, is_anonymous) = random_operator

            self.assertEqual(operator.email, email)
            self.assertEqual(operator.password, password)
            self.assertEqual(operator.is_active, is_active)
            self.assertEqual(operator.authenticated, False)
            self.assertEqual(operator.is_anonymous, is_anonymous)

    @staticmethod
    def generator_random_operator():
        from faker import Faker
        from gooutsafe.models import Operator

        faker = Faker()

        email = faker.email()
        password = faker.password()
        is_active = faker.boolean()
        is_admin = faker.boolean()
        authenticated = faker.boolean()
        is_anonymous = faker.boolean()

        operator = Operator(email=email, password=password,
                            is_active=is_active,
                            is_admin=is_admin,
                            authenticated=authenticated,
                            is_anonymous=is_anonymous
                            )
        return operator, (email, password, is_active, is_admin, is_anonymous)


