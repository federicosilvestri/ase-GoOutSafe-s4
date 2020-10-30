from gooutsafe.models.reservation import Reservation
from .manager import Manager


class ReservationManager(Manager):

    @staticmethod
    def create_reservation(reservation: Reservation):
        Manager.create(reservation=reservation)

    @staticmethod
    def retrieve_by_id(id_):
        Manager.check_none(id=id_)
        return Reservation.query.get(id_)

    @staticmethod
    def retrieve_by_restaurant_id(restaurant_id):
        Manager.check_none(restaurant_id=restaurant_id)
        return Reservation.query.filter(Reservation.restaurant_id==restaurant_id)

    @staticmethod
    def update_reservation(reservation: Reservation):
        Manager.update(reservation=reservation)

    @staticmethod
    def delete_reservation(reservation: Reservation):
        Manager.delete(reservation=reservation)

    @staticmethod
    def delete_reservation_by_id(id_: int):
        reservation = ReservationManager.retrieve_by_id(id_)
        ReservationManager.delete_reservation(reservation)
