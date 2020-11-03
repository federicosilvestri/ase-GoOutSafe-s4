from faker import Faker
from models.test_customer import TestCustomer

from .dao_test import DaoTest


class TestCustomerManager(DaoTest):
    faker = Faker('it_IT')

    def setUp(self):
        super(TestCustomerManager, self).setUp()

        from gooutsafe.dao import customer_manager
        self.customer_manager = customer_manager.CustomerManager
    
    def test_create_customer(self):
        customer1, _ = TestCustomer.generate_random_customer()
        self.customer_manager.create_customer(customer=customer1)
        customer2 = self.customer_manager.retrieve_by_id(id_=customer1.id)
        TestCustomer.assertEqualCustomers(customer1, customer2)

    def test_retrieve_customer(self):
        customer1, _ = TestCustomer.generate_random_customer()
        self.customer_manager.create_customer(customer=customer1)
        customer_ssn = self.customer_manager.retrieve_by_ssn(ssn=customer1.social_number)
        customer_email = self.customer_manager.retrieve_by_email(email=customer1.email)
        customer_phone = self.customer_manager.retrieve_by_phone(phone=customer1.phone)
        #tests for existing customers
        TestCustomer.assertEqualCustomers(customer1, customer_ssn)
        TestCustomer.assertEqualCustomers(customer1, customer_email)
        TestCustomer.assertEqualCustomers(customer1, customer_phone)
        #tests for nonexisting customers in the database
        customer_fake, _ = TestCustomer.generate_random_customer()
        customer_ssn = self.customer_manager.retrieve_by_ssn(ssn=customer_fake.social_number)
        customer_email = self.customer_manager.retrieve_by_email(email=customer_fake.email)
        customer_phone = self.customer_manager.retrieve_by_phone(phone=customer_fake.phone)
        self.assertIsNone(customer_ssn)
        self.assertIsNone(customer_email)
        self.assertIsNone(customer_phone)

    def test_retrieve_positive_customers(self):
        pos_customers = self.customer_manager.retrieve_all_positive()
        if(pos_customers is not None):
            for customers in pos_customers:
                self.assertTrue(customers.health_status)
    
    def test_delete_customer(self):
        base_customer, _ = TestCustomer.generate_random_customer()
        self.customer_manager.create_customer(customer=base_customer)
        self.customer_manager.delete_customer(base_customer)
        self.assertIsNone(self.customer_manager.retrieve_by_id(base_customer.id))

    def test_delete_customer_by_id(self):
        base_customer, _ = TestCustomer.generate_random_customer()
        self.customer_manager.create_customer(customer=base_customer)
        self.customer_manager.delete_customer_by_id(base_customer.id)
        self.assertIsNone(self.customer_manager.retrieve_by_id(base_customer.id))

    def test_update_customer(self):
        base_customer, _ = TestCustomer.generate_random_customer()
        self.customer_manager.create_customer(customer=base_customer)
        base_customer.set_social_number(TestCustomerManager.faker.ssn())
        base_customer.set_firstname(TestCustomerManager.faker.first_name())
        self.customer_manager.update_customer(customer=base_customer)
        updated_customer = self.customer_manager.retrieve_by_id(id_=base_customer.id)
        TestCustomer.assertEqualCustomers(base_customer, updated_customer)


        
