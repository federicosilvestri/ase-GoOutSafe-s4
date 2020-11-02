from gooutsafe.models.reservation import Reservation
from .manager import Manager
from gooutsafe import db


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
        return Reservation.query.filter(Reservation.restaurant_id==restaurant_id).all()

    @staticmethod
    def retrieve_by_customer_id(user_id):
        Manager.check_none(user_id=user_id)
        return Reservation.query.filter(Reservation.user_id==user_id).all()

    @staticmethod
    def retrieve_all_contact_reservation_by_id(id_):
        Manager.check_none(id=id_)
        pos_reservation = ReservationManager.retrieve_by_id(id_)
        cond1 = db.and_(Reservation.start_time <= pos_reservation.start_time, pos_reservation.start_time < Reservation.end_time)
        cond2 = db.and_(Reservation.start_time < pos_reservation.end_time, pos_reservation.end_time < Reservation.end_time)
        cond3 = db.or_(cond1,cond2)
        cond4 = db.and_(cond3, Reservation.restaurant_id==pos_reservation.restaurant_id)
        return Reservation.query.filter(cond4).all()[1::]

    @staticmethod
    def retrieve_by_table_id(table_id):
        Manager.check_none(table_id=table_id)
        return Reservation.query.filter(Reservation.table_id==table_id).all()

    @staticmethod
    def update_reservation(reservation: Reservation):
        Manager.check_none(reservation=reservation)
        Manager.update(reservation=reservation)

    @staticmethod
    def delete_reservation(reservation: Reservation):
        Manager.check_none(reservation=reservation)
        Manager.delete(reservation=reservation)

    @staticmethod
    def delete_reservation_by_id(id_: int):
        reservation = ReservationManager.retrieve_by_id(id_)
        ReservationManager.delete_reservation(reservation)
