from faker import Faker
from datetime import timedelta, datetime
from models.test_reservation import TestReservation

from .dao_test import DaoTest


class TestReservationManager(DaoTest):
    faker = Faker('it_IT')

    def setUp(self):
        super(TestReservationManager, self).setUp()

        from gooutsafe.dao import reservation_manager
        self.reservation_manager = reservation_manager.ReservationManager
    
    def test_create_reservation(self):
        resevation1, _ = TestReservation.generate_random_reservation()
        self.reservation_manager.create_reservation(reservation=resevation1)
        resevation2 = self.reservation_manager.retrieve_by_id(id_=resevation1.id)
        TestReservation.assertEqualReservations(resevation1, resevation1)

    def test_delete_reservation(self):
        base_reservation, _ = TestReservation.generate_random_reservation()
        self.reservation_manager.create_reservation(reservation=base_reservation)
        self.reservation_manager.delete_reservation(base_reservation)
        self.assertIsNone(self.reservation_manager.retrieve_by_id(base_reservation.id))

    def test_delete_reservation_by_id(self):
        base_reservation, _ = TestReservation.generate_random_reservation()
        self.reservation_manager.create_reservation(reservation=base_reservation)
        self.reservation_manager.delete_reservation_by_id(base_reservation.id)
        self.assertIsNone(self.reservation_manager.retrieve_by_id(base_reservation.id))

    def test_update_reservation(self):
        base_reservation, _ = TestReservation.generate_random_reservation()
        self.reservation_manager.create_reservation(reservation=base_reservation)
        base_reservation.set_people_number(TestReservationManager.faker.random_int(max=15))
        start_time = TestReservationManager.faker.date_time_between('now','+6w')
        base_reservation.set_start_time(start_time)
        updated_reservation = self.reservation_manager.retrieve_by_id(id_=base_reservation.id)
        TestReservation.assertEqualReservations(base_reservation, updated_reservation)