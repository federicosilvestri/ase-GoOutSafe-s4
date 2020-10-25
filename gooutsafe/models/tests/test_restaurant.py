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
        

if __name__ == '__main__':
    unittest.main()
