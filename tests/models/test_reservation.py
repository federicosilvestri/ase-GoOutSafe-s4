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

        self.reservation = reservation
        self.table = table
        self.user = user

    def test_reservation_init(self):
        start_time = datetime(2020, 12, 26, 13)
        user = self.user.User()
        table = self.table.Table(3, "Pizza da Stefano")
        reservation = self.reservation.Reservation(user, table, start_time)
        self.assertEqual(reservation.user, user)
        self.assertEqual(reservation.table, table)
        self.assertEqual(reservation.start_time, start_time)
        end_time = start_time + timedelta(hours=3)
        self.assertEqual(reservation.end_time, end_time)

    def test_start_time(self, start_time):
        start_time = datetime(2020, 10, 26, 13)
        user = self.user.User()
        table = self.table.Table(3, "Pizza da Stefano")
        with self.assertRaises(ValueError):
            reservation = self.reservation.Reservation(user, table, start_time)
            print(reservation.actual_time)


if __name__ == '__main__':
    unittest.main()
