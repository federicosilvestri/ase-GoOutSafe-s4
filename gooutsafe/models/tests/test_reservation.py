import unittest
from datetime import datetime
from datetime import timedelta

from gooutsafe.models.reservation import Reservation
from gooutsafe.models.table import Table
from gooutsafe.models.user import User


class TestReservation(unittest.TestCase):

    def test_reservation_init(self):
        start_time = datetime(2020, 12, 26, 13)
        user = User()
        table = Table(3, "Pizza da Stefano")
        reservation = Reservation(user, table, start_time)
        self.assertEqual(reservation.user, user)
        self.assertEqual(reservation.table, table)
        self.assertEqual(reservation.start_time, start_time)
        end_time =  start_time + timedelta(hours=3)
        self.assertEqual(reservation.end_time, end_time)

    def test_start_time(self, start_time):
        start_time = datetime(2020, 10, 26, 13)
        user = User()
        table = Table(3, "Pizza da Stefano")
        with self.assertRaises(ValueError):
            reservation = Reservation(user, table, start_time)
            print(reservation.actual_time)


if __name__ == '__main__':
    unittest.main()
