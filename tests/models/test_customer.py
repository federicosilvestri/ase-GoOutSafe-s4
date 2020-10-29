import unittest
from datetime import datetime

from faker import Faker

from .model_test import ModelTest


class TestCustomer(ModelTest):

    faker = Faker('it_IT')

    def setUp(self):
        super(TestCustomer, self).setUp()
        from gooutsafe.models import customer
        self.customer = customer

    def test_cust_init(self):
        for i in range(0, 10):
            customer, (name, surname, password, email, birthdate, social_number, health_status) = TestCustomer.generate_random_customer()

            self.assertEqual(customer.email, email)
            self.assertEqual(customer.firstname, name)
            self.assertEqual(customer.lastname, surname)
            self.assertEqual(customer.birthday, birthdate)
            self.assertEqual(customer.social_number, social_number)
            self.assertEqual(customer.health_status, health_status)

    @staticmethod
    def assertEqualCustomers(c1, c2):
        t = unittest.FunctionTestCase(TestCustomer)
        t.assertEqual(c1.firstname, c2.firstname)
        t.assertEqual(c1.lastname, c2.lastname)
        t.assertEqual(c1.birthday, c2.birthday)
        t.assertEqual(c1.social_number, c2.social_number)
        t.assertEqual(c1.health_status, c2.health_status)

    @staticmethod
    def generate_random_customer():
        import datetime
        from datetime import date

        from gooutsafe.models import Customer


        complete_name = TestCustomer.faker.name().split(' ')
        name, surname = complete_name[::len(complete_name) - 1]
        password = TestCustomer.faker.password()
        email = TestCustomer.faker.email()
        birthdate = date.fromisoformat(TestCustomer.faker.date(end_datetime=date.today() - datetime.timedelta(days= 365 * 20)))
        social_number = TestCustomer.faker.ssn()
        health_status = TestCustomer.faker.boolean()
        

        customer = Customer(
            firstname=name,
            lastname=surname,
            email=email,
            password=password,
            birthday=birthdate,
            social_number=social_number,
            health_status=health_status
        )

        return customer, (name, surname, password, email, birthdate, social_number, health_status)

    def test_valid_social_number(self):
        customer, _ = TestCustomer.generate_random_customer()
        social_number = TestCustomer.faker.ssn()
        customer.set_social_number(social_number)
        self.assertEqual(customer.social_number, social_number)

    def test_invalid_social_number(self):
        customer, _ = TestCustomer.generate_random_customer()
        social_number = ''.join(['%s' % i for i in range(0, self.customer.Customer.SOCIAL_CODE_LENGTH + 1)])
        with self.assertRaises(ValueError):
            customer.set_social_number(social_number)
