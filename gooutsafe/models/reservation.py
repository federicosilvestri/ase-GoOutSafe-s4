from datetime import timedelta
import datetime
from sqlalchemy.orm import relationship

from gooutsafe import db


class Reservation(db.Model):
    __tablename__ = 'Reservation'

    MAX_TIME_RESERVATION = 3

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    user = relationship('User', foreign_keys='Reservation.user_id')
    table_id = db.Column(db.Integer, db.ForeignKey('Table.id'))
    table = relationship('Table')
    restaurant_id = db.Column(db.Integer, db.ForeignKey('Restaurant.id'))
    restaurant = relationship("Restaurant", back_populates="reservations")
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)

    def __init__(self, user, table, restaurant, start_time, end_time=None):
        self.user = user
        self.table = table
        self.restaurant = restaurant
        self.start_time = start_time

        if end_time is None:
            # end_time will be set automatically as start_time + 3 hours
            self.end_time = start_time + timedelta(hours=self.MAX_TIME_RESERVATION)
        else:
            Reservation.check_time(start_time, end_time)
            self.end_time = end_time

    @staticmethod
    def check_time(start_time, end_time):
        if start_time >= end_time:
            raise ValueError('The start time cannot be greater than end_time')

    def set_user(self, user):
        self.user = user

    def set_table(self, table):
        self.table = table
    
    def set_restaurant(self, restaurant):
        self.restaurant = restaurant

    def set_start_time(self, start_time):
        Reservation.check_time(start_time, self.end_time)
        self.timestamp = datetime.datetime.now()
    
    def get_end_time(self):
        return self.__end_time
    
    def set_end_time(self, end_time):
        Reservation.check_time(self.start_time, end_time)
        self.end_time = end_time
