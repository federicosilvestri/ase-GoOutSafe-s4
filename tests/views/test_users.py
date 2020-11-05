from .view_test import ViewTest
from faker import Faker
import datetime
import unittest

class TestUsers(ViewTest):

    faker = Faker('it_IT')

    @classmethod
    def setUpClass(cls):
        super(TestUsers, cls).setUpClass()

    def test_create_user(self):
        #create an operator
        data = {'email': TestUsers.faker.email(), 'password': TestUsers.faker.password()}
        rv = self.client.post('/create_user/operator', data=data, follow_redirects=True)
        assert rv.status_code == 200
        #create a  new customer
        social_number = TestUsers.faker.ssn()
        email = TestUsers.faker.email()
        name = 'Charlie'
        surname = 'Brown'
        password = TestUsers.faker.password()
        birthdate = datetime.date(year=1992,month=12,day=12)
        phone = TestUsers.faker.phone_number()
        data = {'email': email, 'password': password, 'social_number': social_number, 'firstname': name, 'lastname': surname, 'birthdate': birthdate, 'phone':phone}
        rv = self.client.post('/create_user/customer', data=data, follow_redirects=True)
        assert rv.status_code == 200
        # create same customer
        rv = self.client.post('/create_user/customer', data=data)
        assert rv.status_code == 200
        #create customer with wrong birthdate
        data = {'email': email, 'password': password, 'social_number': social_number, 'firstname': name, 'lastname': surname, 'birthdate': "", 'phone':phone}
        rv = self.client.post('/create_user/customer', data=data, follow_redirects=True)
        assert rv.status_code == 200

    def test_delete_user(self):
        #delete a customer
        customer = self.login_test_customer()
        rv = self.client.post('/delete_user/'+str(customer.id), follow_redirects=True)
        assert rv.status_code == 200
        #delete an operator
        operator = self.login_test_operator()
        rv = self.client.post('/delete_user/'+str(operator.id), follow_redirects=True)

