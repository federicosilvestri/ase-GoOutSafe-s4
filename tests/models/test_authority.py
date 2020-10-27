import unittest


class TestAuthority(unittest.TestCase):

    def setUp(self):
        from gooutsafe import create_app
        create_app('config.TestConfig')

        from gooutsafe.models import health_authority
        self.health_authority = health_authority

    def test_cust_init(self):
        authority = self.health_authority.Authority(email='authority@authority.com', password='admin', name='ASL1',
                                                    city='Pisa',
                                                    address='Largo Bruno Pontecorvo 3', phone='050 221 2111')

        self.assertEqual(authority.email, 'authority@authority.com')
        self.assertEqual(authority.name, 'ASL1')
        self.assertEqual(authority.city, 'Pisa')
        self.assertEqual(authority.address, 'Largo Bruno Pontecorvo 3')
        self.assertEqual(authority.phone, '050 221 2111')


if __name__ == '__main__':
    unittest.main()
