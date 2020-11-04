from flask import url_for
from faker import Faker

from tests.models.test_reservation import TestReservation


from tests.views.view_test import ViewTest


class TestReservationView(ViewTest):
    faker = Faker()

    def setUp(self):
        super(TestReservationView, self).setUp()

        from gooutsafe.views import reservation
        from gooutsafe.views import home

        from gooutsafe.dao import reservation_manager
        self.reservation_manager = reservation_manager.ReservationManager



    """
    def test_create_reservation(self):
        pass
        #TODO: implement

    def test_home(self):
        result = self.app.get('/') 
        self.assertEqual(result.status_code, 200) 
    

    def test_reservation_details(self):
        reservation, _ = TestReservation.generate_random_reservation()
        self.reservation_manager.create_reservation(reservation)
        reservation_id = reservation.id
        restaurant_id = reservation.restaurant_id


       
        with self.app.app_context():
            response = self.client.post(url_for(
                'reservation.reservation_details', restaurant_id = restaurant_id, reservation_id = reservation_id
                )
            )
            print(str(response.status_code) + '********************')
            self.assertEqual(response, 'reservation_details.html')
    """
