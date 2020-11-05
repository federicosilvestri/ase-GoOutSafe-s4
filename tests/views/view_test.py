import unittest


class ViewTest(unittest.TestCase):
    """
    This class should be implemented by
    all classes that tests views
    """
    client = None

    @classmethod
    def setUpClass(cls):
        from gooutsafe import create_app
        app = create_app()
        cls.client = app.test_client()
        from tests.models.test_customer import TestCustomer
        cls.test_customer = TestCustomer
        from gooutsafe.dao import customer_manager
        cls.customer_manager = customer_manager.CustomerManager

    #simulate the login for testing the views with @login_required
    def login_test(self):
        customer, _ = self.test_customer.generate_random_customer()
        psw = customer.password
        customer.set_password(customer.password)
        self.customer_manager.create_customer(customer=customer)
        data = {'email': customer.email, 'password': psw}
        self.client.post('/login', data=data)
        return customer

    
