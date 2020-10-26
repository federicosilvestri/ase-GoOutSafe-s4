import unittest
from gooutsafe.models.restaurant import Restaurant


class TestRestaurant(unittest.TestCase):

    def test_rest_init(self):
        restaurant = Restaurant('Quello Buono', 10, 20, 55555555, 'Vegetarian')
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
        with self.assertRaises(ValueError):
            restaurant = Restaurant(long_name, 10, 20, 55555555, 'Vegetarian')
       
    def test_short_name(self):
        short_name = ""
        with self.assertRaises(ValueError):
            restaurant = Restaurant(short_name, 10, 20, 55555555, 'Vegetarian')
    
    def test_too_high_lat1(self):
        lat = 1000
        with self.assertRaises(ValueError):
            restaurant = Restaurant("name", lat, 20, 55555555, 'Vegetarian')
    
    def test_too_high_lat2(self):
        lat = 86
        with self.assertRaises(ValueError):
            restaurant = Restaurant("name", lat, 20, 55555555, 'Vegetarian')
    
    def test_too_low_lat1(self):
        lat = -1000
        with self.assertRaises(ValueError):
            restaurant = Restaurant("name", lat, 20, 55555555, 'Vegetarian')
    
    def test_too_low_lat2(self):
        lat = -86
        with self.assertRaises(ValueError):
            restaurant = Restaurant("name", lat, 20, 55555555, 'Vegetarian')
    
    def test_too_high_lon1(self):
        lon = 1000
        with self.assertRaises(ValueError):
            restaurant = Restaurant("name", 10, lon, 55555555, 'Vegetarian')
    
    def test_too_high_lon2(self):
        lon = 181
        with self.assertRaises(ValueError):
            restaurant = Restaurant("name", 10, lon, 55555555, 'Vegetarian')
    
    def test_too_low_lon1(self):
        lon = -1000
        with self.assertRaises(ValueError):
            restaurant = Restaurant("name", 10, lon, 55555555, 'Vegetarian')

    def test_too_low_lon2(self):
        lon = -181
        with self.assertRaises(ValueError):
            restaurant = Restaurant("name", 10, lon, 55555555, 'Vegetarian')

    def test_too_high_phone1(self):
        phone = 99999999999
        with self.assertRaises(ValueError):
            restaurant = Restaurant("name", 10, 10, phone, 'Vegetarian')

    def test_too_high_phone2(self):
        phone = 10000000000
        with self.assertRaises(ValueError):
            restaurant = Restaurant("name", 10, 10, phone, 'Vegetarian')

    def test_too_low_phone1(self):
        phone = -102938102
        with self.assertRaises(ValueError):
            restaurant = Restaurant("name", 10, 10, phone, 'Vegetarian')

    def test_too_low_phone2(self):
        phone = -1
        with self.assertRaises(ValueError):
            restaurant = Restaurant("name", 10, 10, phone, 'Vegetarian')


    def test_long_menu_type(self):
        long_name = """AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
            AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"""
        with self.assertRaises(ValueError):
            restaurant = Restaurant("name", 10, 20, 55555555, long_name)
       
    def test_short_menu_type(self):
        short_name = ""
        with self.assertRaises(ValueError):
            restaurant = Restaurant("name", 10, 20, 55555555, short_name)
    
    def test_is_open_default(self):
        restaurant = Restaurant("name", 10, 20, 55555555, "menu")
        self.assertEqual(restaurant.is_open, False)
    
    def test_is_open_false(self):
        restaurant = Restaurant("name", 10, 20, 55555555, "menu")
        restaurant.is_open = True
        restaurant.is_open = False
        self.assertEqual(restaurant.is_open, False)

    def test_is_open_true(self):
        restaurant = Restaurant("name", 10, 20, 55555555, "menu")
        restaurant.is_open = True
        self.assertEqual(restaurant.is_open, True)

if __name__ == '__main__':
    unittest.main()
