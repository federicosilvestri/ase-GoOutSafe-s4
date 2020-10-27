import unittest
from datetime import datetime

class TestCustomer(unittest.TestCase):

    def setUp(self):
        from gooutsafe import create_app
        create_app('config.TestConfig')

        from gooutsafe.models import customer
        self.customer = customer

    def test_cust_init(self):
        birthday = datetime(1995, 12, 31)
        customer = self.customer.Customer(email='example@example.com', password='admin', firstname='example_name',
                                          lastname='example_lastname',
                                          birthday=birthday, health_status=False)

        self.assertEqual(customer.email, 'example@example.com')
        self.assertEqual(customer.firstname, 'example_name')
        self.assertEqual(customer.lastname, 'example_lastname')
        self.assertEqual(customer.birthday, birthday)
        self.assertEqual(customer.health_status, False)


if __name__ == '__main__':
    unittest.main()
