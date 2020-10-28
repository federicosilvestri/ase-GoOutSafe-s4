from sqlalchemy.orm import relationship

from gooutsafe import db


class RestaurantAvailability(db.Model):
    __tablename__ = 'Availability'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('Restaurant.id'))
    restaurant = relationship('Restaurant', foreign_keys='Availability.restaurant_id')
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)

    def __init__(self, restaurant_id, start_time, end_time):
        self.restaurant_id = restaurant_id
        self.start_time = start_time
        self.end_time = end_time
