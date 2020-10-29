from .model_test import ModelTest
from datetime import datetime
from datetime import timedelta


class TestReservation(ModelTest):

    def setUp(self):
        super(TestReservation, self).setUp()

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
        reservation = self.reservation.Reservation(user, table, restaurant, start_time, end_time=end_time)
        self.assertEqual(reservation.user, user)
        self.assertEqual(reservation.table, table)
        self.assertEqual(reservation.start_time, start_time) 
        self.assertEqual(reservation.end_time, end_time)

    def test_set_start_time(self):
        user = self.user.User()
        restaurant = self.restaurant.Restaurant('Quello Buono', 10, 20, "55555555", 'Vegetarian')
        table = self.table.Table(3, restaurant.id)
        start_time = datetime(2020, 12, 26, 13)
        resvation = self.reservation.Reservation(user, table, restaurant, start_time, end_time=start_time + timedelta(hours=4))
        wrong_start_time = start_time + timedelta(days=4)
        with self.assertRaises(ValueError):
                resvation.set_start_time(wrong_start_time)
