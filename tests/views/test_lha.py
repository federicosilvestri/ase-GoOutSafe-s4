from tests.views.view_test import ViewTest


class TestLHA(ViewTest):

    def setUp(self):
        super(TestLHA, self).setUp()

    def test_search_customer_redirect(self):
        self.login_test_customer()
        rv = self.client.post('/ha/search_customer')
        self.assertEqual(rv.status_code, 302)

    def test_search_customer_none(self):
        self.login_test_authority()
        rv = self.client.post('/ha/search_customer', data=dict(track_type='SSN', customer_ident='ldl'))
        self.assertEqual(rv.status_code, 302)

    def test_search_customer_with_ssn(self):
        from tests.models.test_customer import TestCustomer
        from gooutsafe.dao.customer_manager import CustomerManager

        customer, (_, _, _, _, _, ssn, _, _) = TestCustomer.generate_random_customer()
        CustomerManager.create_customer(customer=customer)

        self.login_test_authority()
        rv = self.client.post('/ha/search_customer', data=dict(track_type='SSN', customer_ident=ssn))

        self.assertEqual(rv.status_code, 302)

    def test_search_customer_with_email(self):
        from tests.models.test_customer import TestCustomer
        from gooutsafe.dao.customer_manager import CustomerManager

        customer, (_, _, _, email, _, _, _, _) = TestCustomer.generate_random_customer()
        CustomerManager.create_customer(customer=customer)

        self.login_test_authority()
        rv = self.client.post('/ha/search_customer', data=dict(track_type='email', customer_ident=email))

        self.assertEqual(rv.status_code, 302)

    def test_search_customer_with_phone(self):
        from tests.models.test_customer import TestCustomer
        from gooutsafe.dao.customer_manager import CustomerManager

        customer, (_, _, _, _, _, _, _, phone) = TestCustomer.generate_random_customer()
        CustomerManager.create_customer(customer=customer)

        self.login_test_authority()
        rv = self.client.post('/ha/search_customer', data=dict(track_type='email', customer_ident=phone))

        self.assertEqual(rv.status_code, 302)

    def test_mark_positive_unauthorized(self):
        self.login_test_customer()
        rv = self.client.post('ha/mark_positive/2')
        self.assertEqual(rv.status_code, 302)

    def test_mark_positive_authorized_inex(self):
        self.login_test_authority()
        rv = self.client.post('ha/mark_positive/2')
        self.assertEqual(rv.status_code, 302)

    def test_mark_positive(self):
        """ we cannot test it without redis"""
        """
        from tests.models.test_customer import TestCustomer
        from gooutsafe.dao.customer_manager import CustomerManager

        customer, (_, _, _, _, _, _, _, phone) = TestCustomer.generate_random_customer()
        CustomerManager.create_customer(customer=customer)

        self.login_test_authority()
        rv = self.client.post('ha/mark_positive/1')
        self.assertEqual(rv.status_code, 302)
        """
        pass
