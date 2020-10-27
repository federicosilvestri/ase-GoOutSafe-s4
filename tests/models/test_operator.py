import unittest


class TestOperator(unittest.TestCase):

    def setUp(self):
        from gooutsafe import create_app
        create_app('config.TestConfig')

        from gooutsafe.models import operator
        self.operator = operator

    def test_cust_init(self):
        operator = self.operator.Operator(email='operator@operator.com', password='admin')
        self.assertEqual(operator.email, 'operator@operator.com')


if __name__ == '__main__':
    unittest.main()
