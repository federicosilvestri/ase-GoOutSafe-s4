import random
import string

from faker import Faker

from .model_test import ModelTest


class TestRestaurant(ModelTest):
    faker = Faker()

    def setUp(self):
        super(TestRestaurant, self).setUp()

        from gooutsafe.models import restaurant
        self.restaurant = restaurant

    @staticmethod
    def generate_random_restaurant():
        from gooutsafe.models.restaurant import Restaurant

        name = TestRestaurant.faker.company()
        lat = TestRestaurant.faker.latitude()
        lon = TestRestaurant.faker.longitude()
        phone = TestRestaurant.faker.phone_number()
        menu_type = TestRestaurant.faker.country()

        restaurant = Restaurant(
            name=name,
            lat=lat,
            lon=lon,
            phone=phone,
            menu_type=menu_type
        )

        return restaurant, (name, lat, lon, phone, menu_type)

    def test_rest_init(self):
        for _ in range(0, 10):
            restaurant, (name, lat, lon, phone, menu_type) = TestRestaurant.generate_random_restaurant()

            self.assertEqual(restaurant.name, name)
            self.assertEqual(restaurant.lat, lat)
            self.assertEqual(restaurant.lon, lon)
            self.assertEqual(restaurant.phone, phone)
            self.assertEqual(restaurant.menu_type, menu_type)

    def test_valid_name(self):
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        name = TestRestaurant.faker.company()
        restaurant.set_name(name)
        self.assertEqual(restaurant.name, name)

    def test_long_name(self):
        long_name = ''.join(
            random.choice(string.ascii_letters) for _ in
            range(0, self.restaurant.Restaurant.MAX_NAME_LENGTH + random.randint(1, 100))
        )

        restaurant, _ = TestRestaurant.generate_random_restaurant()
        with self.assertRaises(ValueError):
            restaurant.set_name(long_name)

    def test_short_name(self):
        short_name = ""
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        with self.assertRaises(ValueError):
            restaurant.set_name(short_name)
    
    def test_valid_lat(self):
        lat = TestRestaurant.faker.latitude()
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        restaurant.set_lat(lat)
        self.assertEqual(restaurant.lat, lat)

    def test_too_high_lat1(self):
        lat = 1000
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        with self.assertRaises(ValueError):
            restaurant.set_lat(lat)

    def test_too_high_lat2(self):
        lat = 86
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        with self.assertRaises(ValueError):
            restaurant.set_lat(lat)

    def test_too_low_lat1(self):
        lat = -1000
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        with self.assertRaises(ValueError):
            restaurant.set_lat(lat)

    def test_too_low_lat2(self):
        lat = -86
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        with self.assertRaises(ValueError):
            restaurant.set_lat(lat)

    def test_valid_lon(self):
        lon = TestRestaurant.faker.longitude()
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        restaurant.set_lon(lon)
        self.assertEqual(restaurant.lon, lon)

    def test_too_high_lon1(self):
        lon = 1000
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        with self.assertRaises(ValueError):
            restaurant.set_lon(lon)

    def test_too_high_lon2(self):
        lon = 181
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        with self.assertRaises(ValueError):
            restaurant.set_lon(lon)

    def test_too_low_lon1(self):
        lon = -1000
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        with self.assertRaises(ValueError):
            restaurant.set_lon(lon)

    def test_too_low_lon2(self):
        lon = -181
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        with self.assertRaises(ValueError):
            restaurant.set_lon(lon)

    def test_valid_phone(self):
        phone = TestRestaurant.faker.phone_number()
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        restaurant.set_phone(phone)
        self.assertEqual(restaurant.phone, phone)

    def test_too_high_phone1(self):
        restaurant, _ = TestRestaurant.generate_random_restaurant()

        phone = ''.join(['%s' % i for i in range(0, self.restaurant.Restaurant.MAX_PHONE_LEN + 1)])
        with self.assertRaises(ValueError):
            restaurant.set_phone(phone)

    def test_too_short_phone(self):
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        with self.assertRaises(ValueError):
            phone = ""
            restaurant.set_phone(phone)

    def test_valid_menu_type(self):
        menu_type = TestRestaurant.faker.country()
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        restaurant.set_menu_type(menu_type)
        self.assertEqual(restaurant.menu_type, menu_type)

    def test_long_menu_type(self):
        long_name = ''.join(
            random.choice(string.ascii_letters) for _ in
            range(0, self.restaurant.Restaurant.MAX_MENU_TYPE_LENGTH + random.randint(1, 100))
        )

        restaurant, _ = TestRestaurant.generate_random_restaurant()
        with self.assertRaises(ValueError):
            restaurant.set_menu_type(long_name)

    def test_short_menu_type(self):
        short_name = ""
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        with self.assertRaises(ValueError):
            restaurant.set_menu_type(short_name)

    def test_is_open_default(self):
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        self.assertEqual(restaurant.is_open, False)

    def test_is_open_false(self):
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        restaurant.set_is_open(False)
        self.assertEqual(restaurant.is_open, False)

    def test_is_open_true(self):
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        restaurant.set_is_open(True)
        self.assertEqual(restaurant.is_open, True)
