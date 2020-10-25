from sqlalchemy.orm import relationship

from gooutsafe import db


class Table(db.Model):
    __tablename__ = 'Table'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('Restaurant.id'))
    restaurant = relationship('Restaurant', foreign_keys='Table.restaurant_id')
    capacity = db.Column(db.Integer)
    reservation_id = db.Column(db.Integer, db.ForeignKey('Reservation.id'))
    reservations = relationship("Reservation", foreign_keys='Table.reservation_id')

    def __init__(self, capacity, restaurant):
        self.capacity = capacity
        self.restaurant = restaurant
