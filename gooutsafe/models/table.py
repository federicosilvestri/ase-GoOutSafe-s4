from sqlalchemy.orm import relationship

from gooutsafe.database import db


class Table(db.Model):
    __tablename__ = 'Table'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    restaurant_id = relationship('Restaurant', foreign_keys='restaurant.restaurant_id')
    capacity = db.Column(db.Integer)
    reservations = relationship("Reservations")

    def __init__(self, id, capacity, restaurant):
        self.id = id
        self.capacity = capacity
        self.restaurant = restaurant
