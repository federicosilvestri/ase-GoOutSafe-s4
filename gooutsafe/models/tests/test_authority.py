import unittest

# from gooutsafe.models.user import User
from gooutsafe.models.health_authority import Authority


class TestAuthority(unittest.TestCase):

    def test_cust_init(self):
        authority = Authority(email='authority@authority.com', password='admin', name='ASL1', city='Pisa',
                              address='Largo Bruno Pontecorvo 3', phone='050 221 2111')

        self.assertEqual(authority.email, 'authority@authority.com')
        self.assertEqual(authority.name, 'ASL1')
        self.assertEqual(authority.city, 'Pisa')
        self.assertEqual(authority.address, 'Largo Bruno Pontecorvo 3')
        self.assertEqual(authority.phone, '050 221 2111')


if __name__ == '__main__':
    unittest.main()
