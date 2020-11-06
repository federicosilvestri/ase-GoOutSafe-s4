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
        from tests.models.test_operator import TestOperator
        cls.test_operator = TestOperator
        from gooutsafe.dao import operator_manager
        cls.operator_manager = operator_manager.OperatorManager
        from tests.models.test_authority import TestAuthority
        cls.test_authority = TestAuthority
        from gooutsafe.dao import health_authority_manager
        cls.authority_manager = health_authority_manager.AuthorityManager

    #simulate the customer login for testing the views with @login_required
    def login_test_customer(self):
        customer, _ = self.test_customer.generate_random_customer()
        psw = customer.password
        customer.set_password(customer.password)
        self.customer_manager.create_customer(customer=customer)
        data = {'email': customer.email, 'password': psw}
        self.client.post('/login', data=data)
        return customer

    #simulate the operator login for testing the views with @login_required
    def login_test_operator(self):
        operator, _ = self.test_operator.generate_random_operator()
        psw = operator.password
        operator.set_password(operator.password)
        self.operator_manager.create_operator(operator=operator)
        data = {'email': operator.email, 'password': psw}
        self.client.post('/login', data=data)
        return operator
    
        

    
