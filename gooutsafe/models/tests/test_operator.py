import unittest

# from gooutsafe.models.user import User
from gooutsafe.models.operator import Operator


class TestOperator(unittest.TestCase):

    def test_cust_init(self):
        operator = Operator(email='operator@operator.com', password='admin')
        self.assertEqual(operator.email, 'operator@operator.com')


if __name__ == '__main__':
    unittest.main()
