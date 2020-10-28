from .model_test import ModelTest


class TestAuthority(ModelTest):

    def setUp(self):
        super(TestAuthority, self).setUp()

        from gooutsafe.models import health_authority
        self.health_authority = health_authority

    def test_cust_init(self):
        for i in range(0, 10):
            authority, (email, city, password, name, address, phone) = TestAuthority.generate_random_authority()

            self.assertEqual(authority.email, email)
            self.assertEqual(authority.name, name)
            self.assertEqual(authority.city, city)
            self.assertEqual(authority.address, address)
            self.assertEqual(authority.phone, phone)

    @staticmethod
    def generate_random_authority():
        from faker import Faker
        from gooutsafe.models.health_authority import Authority
        faker = Faker()

        email = faker.email()
        city = faker.city()
        password = faker.password()
        name = faker.company()
        address = faker.address()
        phone = faker.phone_number()

        authority = Authority(email=email, password=password, name=name,
                              city=city,
                              address=address, phone=phone
                              )
        return authority, (email, city, password, name, address, phone)
