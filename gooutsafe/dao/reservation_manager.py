from gooutsafe.models.reservation import Reservation
from gooutsafe import db
from .manager import Manager

#CRUD: Create Retrieve Update Delete
class ReservationManager(Manager):

    @staticmethod
    def create_reservation(reservation: Reservation):
        Manager.create(reservation=reservation)

    @staticmethod
    def retrieve_by_id(id_):
        Manager.check_none(id=id_)
        return Reservation.query.get(id_)

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
