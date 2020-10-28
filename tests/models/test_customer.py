from datetime import datetime

from .model_test import ModelTest


class TestCustomer(ModelTest):

    def setUp(self):
        super(TestCustomer, self).setUp()
        from gooutsafe.models import customer
        self.customer = customer

    def test_cust_init(self):
        for i in range(0, 10):
            customer, (name, surname, password, email, birthdate, health_status) = TestCustomer.generate_random_customer()

            self.assertEqual(customer.email, email)
            self.assertEqual(customer.firstname, name)
            self.assertEqual(customer.lastname, surname)
            self.assertEqual(customer.birthday, birthdate)
            self.assertEqual(customer.health_status, health_status)

    @staticmethod
    def generate_random_customer():
        from faker import Faker
        import datetime
        from datetime import date
        from gooutsafe.models import Customer

        faker = Faker()

        complete_name = faker.name().split(' ')
        name, surname = complete_name[::len(complete_name) - 1]
        password = faker.password()
        email = faker.email()
        birthdate = faker.date(end_datetime=date.today() - datetime.timedelta(days= 365 * 20))
        health_status = faker.boolean()

        customer = Customer(
            firstname=name,
            lastname=surname,
            email=email,
            password=password,
            birthday=birthdate,
            health_status=health_status
        )

        return customer, (name, surname, password, email, birthdate, health_status)
