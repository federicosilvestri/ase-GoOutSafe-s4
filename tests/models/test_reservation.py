from .model_test import ModelTest
from datetime import datetime
from datetime import timedelta
from .test_restaurant import  TestRestaurant


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

        # TODO: update the creation of test restaurants by importing the test_restaurant file and 
        #using the generate_random_restaurant() static method
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        table = self.table.Table(3, restaurant)
        reservation = self.reservation.Reservation(user, table, restaurant, 5,start_time, end_time=end_time)
        self.assertEqual(reservation.user, user)
        self.assertEqual(reservation.table, table)
        self.assertEqual(reservation.start_time, start_time) 
        self.assertEqual(reservation.end_time, end_time)

    def test_set_start_time(self):
        user = self.user.User()
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        table = self.table.Table(3, restaurant)
        start_time = datetime(2020, 12, 26, 13)
        resvation = self.reservation.Reservation(user, table, restaurant, 5,start_time, end_time=start_time + timedelta(hours=4))
        wrong_start_time = start_time + timedelta(days=4)
        with self.assertRaises(ValueError):
                resvation.set_start_time(wrong_start_time)
