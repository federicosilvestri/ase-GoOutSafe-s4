import unittest


class TestRestaurant(unittest.TestCase):
    
    def setUp(self):
        from gooutsafe import create_app
        create_app('config.TestConfig')

        from gooutsafe.models import restaurant
        self.restaurant = restaurant

    def test_rest_init(self):
        restaurant = self.restaurant.Restaurant('Quello Buono', 10, 20, 55555555, 'Vegetarian')
        self.assertEqual(restaurant.name, 'Quello Buono')
        self.assertEqual(restaurant.lat, 10)
        self.assertEqual(restaurant.lon, 20)
        self.assertEqual(restaurant.phone, 55555555)
        self.assertEqual(restaurant.menu_type, 'Vegetarian')

    def test_long_name(self):
        long_name = """AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"""
        restaurant = self.restaurant.Restaurant('Quello Buono', 10, 20, 55555555, 'Vegetarian')
        with self.assertRaises(ValueError):
            restaurant.set_name(long_name)

    def test_short_name(self):
        short_name = ""
        restaurant = self.restaurant.Restaurant('Quello Buono', 10, 20, 55555555, 'Vegetarian')
        with self.assertRaises(ValueError):
            restaurant.set_name(short_name)

    def test_too_high_lat1(self):
        lat = 1000
        restaurant = self.restaurant.Restaurant('Quello Buono', 10, 20, 55555555, 'Vegetarian')
        with self.assertRaises(ValueError):
            restaurant.set_lat(lat)
            

    def test_too_high_lat2(self):
        lat = 86
        restaurant = self.restaurant.Restaurant('Quello Buono', 10, 20, 55555555, 'Vegetarian')
        with self.assertRaises(ValueError):
            restaurant.set_lat(lat)

    def test_too_low_lat1(self):
        lat = -1000
        restaurant = self.restaurant.Restaurant('Quello Buono', 10, 20, 55555555, 'Vegetarian')
        with self.assertRaises(ValueError):
            restaurant.set_lat(lat)

    def test_too_low_lat2(self):
        lat = -86
        restaurant = self.restaurant.Restaurant('Quello Buono', 10, 20, 55555555, 'Vegetarian')
        with self.assertRaises(ValueError):
            restaurant.set_lat(lat)

    def test_too_high_lon1(self):
        lon = 1000
        restaurant = self.restaurant.Restaurant('Quello Buono', 10, 20, 55555555, 'Vegetarian')
        with self.assertRaises(ValueError):
            restaurant.set_lon(lon)

    def test_too_high_lon2(self):
        lon = 181
        restaurant = self.restaurant.Restaurant('Quello Buono', 10, 20, 55555555, 'Vegetarian')
        with self.assertRaises(ValueError):
            restaurant.set_lon(lon)

    def test_too_low_lon1(self):
        lon = -1000
        restaurant = self.restaurant.Restaurant('Quello Buono', 10, 20, 55555555, 'Vegetarian')
        with self.assertRaises(ValueError):
            restaurant.set_lon(lon)

    def test_too_low_lon2(self):
        lon = -181
        restaurant = self.restaurant.Restaurant('Quello Buono', 10, 20, 55555555, 'Vegetarian')
        with self.assertRaises(ValueError):
            restaurant.set_lon(lon)

    def test_too_high_phone1(self):
        phone = 99999999999
        restaurant = self.restaurant.Restaurant('Quello Buono', 10, 20, 55555555, 'Vegetarian')
        with self.assertRaises(ValueError):
            restaurant.set_phone(phone)

    def test_too_high_phone2(self):
        phone = 10000000000
        restaurant = self.restaurant.Restaurant('Quello Buono', 10, 20, 55555555, 'Vegetarian')
        with self.assertRaises(ValueError):
            restaurant.set_phone(phone)

    def test_too_low_phone1(self):
        phone = -102938102
        restaurant = self.restaurant.Restaurant('Quello Buono', 10, 20, 55555555, 'Vegetarian')
        with self.assertRaises(ValueError):
            restaurant.set_phone(phone)

    def test_too_low_phone2(self):
        phone = -1
        restaurant = self.restaurant.Restaurant('Quello Buono', 10, 20, 55555555, 'Vegetarian')
        with self.assertRaises(ValueError):
            restaurant.set_phone(phone)

    def test_long_menu_type(self):
        long_name = """AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"""
        restaurant = self.restaurant.Restaurant('Quello Buono', 10, 20, 55555555, 'Vegetarian')
        with self.assertRaises(ValueError):
            restaurant.set_menu_type(long_name)

    def test_short_menu_type(self):
        short_name = ""
        restaurant = self.restaurant.Restaurant('Quello Buono', 10, 20, 55555555, 'Vegetarian')
        with self.assertRaises(ValueError):
            restaurant.set_menu_type(short_name)

    def test_is_open_default(self):
        restaurant = self.restaurant.Restaurant("name", 10, 20, 55555555, "menu")
        self.assertEqual(restaurant.is_open, False)

    def test_is_open_false(self):
        restaurant = self.restaurant.Restaurant("name", 10, 20, 55555555, "menu")
        restaurant.is_open = True
        restaurant.is_open = False
        self.assertEqual(restaurant.is_open, False)

    def test_is_open_true(self):
        restaurant = self.restaurant.Restaurant("name", 10, 20, 55555555, "menu")
        restaurant.is_open = True
        self.assertEqual(restaurant.is_open, True)


if __name__ == '__main__':
    unittest.main()
