from gooutsafe import db
from datetime import datetime

from sqlalchemy.orm import relationship


class RestaurantAvailability(db.Model):
    __tablename__ = 'Availability'

    __id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    __restaurant_id = db.Column(db.Integer, db.ForeignKey('Restaurant.__id'))
    __restaurant = relationship('Restaurant', foreign_keys='Availability.__restaurant_id')
    __start_time = db.Column(db.DateTime)
    __end_time = db.Column(db.DateTime)


    def __init__(self, restaurant_id, start_time, end_time):
        self.__restaurant_id = restaurant_id
        self.__start_time = start_time
        self.__end_time = end_time
