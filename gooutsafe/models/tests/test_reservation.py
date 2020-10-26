import unittest
from datetime import datetime
from datetime import timedelta

from gooutsafe.models.reservation import Reservation
from gooutsafe.models.table import Table
from gooutsafe.models.user import User


class TestReservation(unittest.TestCase):

    def test_reservation_init(self):
        actual_time = datetime(2020, 10, 25, 10)
        start_time = datetime(2020, 10, 26, 13)
        user = User()
        table = Table(3, "Pizza da Stefano")
        reservation = Reservation(user, table, actual_time, start_time)
        self.assertEqual(reservation.user, user)
        self.assertEqual(reservation.table, table)
        self.assertEqual(reservation.timestamp, actual_time)
        self.assertEqual(reservation.start_time, start_time)
        end_time = start_time + timedelta(hours=3)
        print(end_time)
        self.assertEqual(reservation.end_time, end_time)


if __name__ == '__main__':
    unittest.main()
