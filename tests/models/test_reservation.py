import unittest
from datetime import datetime
from datetime import timedelta


class TestReservation(unittest.TestCase):

    def setUp(self):
        from gooutsafe import create_app
        create_app('config.TestConfig')

        from gooutsafe.models import reservation
        from gooutsafe.models import table
        from gooutsafe.models import user
        from gooutsafe.models import restaurant

        self.reservation = reservation
        self.table = table
        self.user = user
        self.restaurant = restaurant

    def test_reservation_init(self):
        start_time = datetime(2020, 12, 26, 13)
        end_time = start_time + timedelta(hours=3)
        user = self.user.User()

        restaurant = self.restaurant.Restaurant('Quello Buono', 10, 20, "55555555", 'Vegetarian')
        table = self.table.Table(3, restaurant.id)
        reservation = self.reservation.Reservation(user, table, start_time, end_time=end_time)
        self.assertEqual(reservation.user, user)
        self.assertEqual(reservation.table, table)
        self.assertEqual(reservation.start_time, start_time) 
        self.assertEqual(reservation.end_time, end_time)

    def test_start_time(self):
        user = self.user.User()
        restaurant = self.restaurant.Restaurant('Quello Buono', 10, 20, "55555555", 'Vegetarian')
        table = self.table.Table(3, restaurant.id)
        wrong_start_time = datetime(2020, 10, 26, 13)
        with self.assertRaises(ValueError):
            self.reservation.Reservation(user, table, wrong_start_time, end_time=wrong_start_time - timedelta(days=4))
            
            

if __name__ == '__main__':
    unittest.main()
