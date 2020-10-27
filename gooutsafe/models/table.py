from sqlalchemy.orm import relationship

from gooutsafe import db


class Table(db.Model):
    __tablename__ = 'Table'

    __id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    __restaurant_id = db.Column(db.Integer, db.ForeignKey('Restaurant.id'))
    __restaurant = relationship('Restaurant', foreign_keys='Table.restaurant_id')
    __capacity = db.Column(db.Integer)
    __reservation_id = db.Column(db.Integer, db.ForeignKey('Reservation.id'))
    __reservations = relationship("Reservation", foreign_keys='Table.reservation_id')

    def __init__(self, capacity, restaurant):
        self.__capacity = capacity
        self.__restaurant = restaurant

    def get_id(self):
        return self.__id

    def get_restaurant_id(self):
        return self.__restaurant_id

    
    def get_capacity(self):
        return self.__capacity
    
    def set_capacity(self, capacity):
        self.__capacity = capacity
        

    def get_reservation_id(self):
        return self.__reservation_id