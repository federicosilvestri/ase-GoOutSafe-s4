from .view_test import ViewTest
from faker import Faker


class TestAuth(ViewTest):

    faker = Faker('it_IT')

    @classmethod
    def setUpClass(cls):
        super(TestAuth, cls).setUpClass()

    def test_get_auth(self):
        #login for a customer
        customer = self.login_test_customer()
        #login with a wrong email
        data = data = {'email': customer.email, 'password': TestAuth.faker.password()}
        assert self.client.post('/login', data=data, follow_redirects=True).status_code == 200
        #login for an operator
        self.login_test_operator()
        #login for non existing customer
        data = {'email': TestAuth.faker.email(), 'password': TestAuth.faker.password()}
        assert self.client.post('/login', data=data, follow_redirects=True).status_code == 200
        #login for an authority
        self.login_test_authority()

