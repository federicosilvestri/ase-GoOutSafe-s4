from sqlalchemy.orm import relationship

from gooutsafe import db


class Table(db.Model):
    __tablename__ = 'Table'

    MAX_TABLE_CAPACITY = 15

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('Restaurant.id', ondelete="CASCADE"))
    restaurant = relationship('Restaurant', back_populates="tables")
    capacity = db.Column(db.Integer)

    def __init__(self, capacity, restaurant):
        self.capacity = capacity
        self.restaurant = restaurant

    def set_capacity(self, capacity):
        if capacity <= 0 or capacity > self.MAX_TABLE_CAPACITY:
            raise ValueError('You can\'t set a negative value, zero or greater than ' 
        + str(self.MAX_TABLE_CAPACITY))
        self.capacity = capacity

    def set_restaurant(self, restaurant):
        self.restaurant = restaurant