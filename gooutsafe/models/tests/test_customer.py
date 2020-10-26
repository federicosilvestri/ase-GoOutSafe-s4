import unittest
#from gooutsafe.models.user import User
from gooutsafe.models.customer import Customer


class TestCustomer(unittest.TestCase):

    def test_cust_init(self):
        customer = Customer(email='example@example.com',password='admin',firstname='example_name', lastname='example_lastname', 
                    date_of_birth='2017-03-02T15:34:10.000272',health_status=False)

        self.assertEqual(customer.email, 'example@example.com')
        self.assertEqual(customer.firstname, 'example_name')
        self.assertEqual(customer.lastname, 'example_lastname')
        self.assertEqual(customer.date_of_birth, '2017-03-02T15:34:10.000272')
        self.assertEqual(customer.health_status, False)
        

if __name__ == '__main__':
    unittest.main()