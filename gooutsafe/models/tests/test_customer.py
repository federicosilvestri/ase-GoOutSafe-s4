import unittest
from gooutsafe.models.user import User
from gooutsafe.models.customer import Customer


class TestCustomer(unittest.TestCase):

    def test_cust_init(self):
        customer = Customer('example@example.com','example_name', 'example_lastname', 
                    '2017-03-02T15:34:10.000272', False)

        self.assertEqual(customer.email, 'example@example.com')
        self.assertEqual(customer.name, 'example_name')
        self.assertEqual(customer.lastname, 'example_lastname')
        self.assertEqual(customer.date_of_birth, '2017-03-02T15:34:10.000272')
        self.assertEqual(customer.health_status, False)
        

if __name__ == '__main__':
    unittest.main()