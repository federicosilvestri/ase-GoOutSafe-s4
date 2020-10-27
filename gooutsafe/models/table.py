from sqlalchemy.orm import relationship

from gooutsafe import db


class Table(db.Model):
    __tablename__ = 'Table'

<<<<<<< HEAD
    __id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    __restaurant_id = db.Column(db.Integer, db.ForeignKey('Restaurant.__id'))
    __restaurant = relationship('Restaurant', foreign_keys='Table.__restaurant_id')
    __capacity = db.Column(db.Integer)
    __reservation_id = db.Column(db.Integer, db.ForeignKey('Reservation.__id'))
    __reservations = relationship("Reservation", foreign_keys='Table.__reservation_id')
=======
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('Restaurant.id'))
    restaurant = relationship('Restaurant', foreign_keys='Table.restaurant_id')
    capacity = db.Column(db.Integer)
    reservation_id = db.Column(db.Integer, db.ForeignKey('Reservation.id'))
    reservations = relationship("Reservation", foreign_keys='Table.reservation_id')
>>>>>>> a3d7a2792655935ded85d6573efabb59ec9b3abd

    def __init__(self, capacity, restaurant):
        self.capacity = capacity
        self.restaurant = restaurant

    def set_capacity(self, capacity):
        self.capacity = capacity
