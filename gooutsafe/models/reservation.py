from datetime import timedelta
import datetime
from sqlalchemy.orm import relationship

from gooutsafe import db


class Reservation(db.Model):
    __tablename__ = 'Reservation'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    user = relationship('User', foreign_keys='Reservation.user_id')
    table_id = db.Column(db.Integer, db.ForeignKey('Table.id'))
    table = relationship('Table', foreign_keys='Reservation.table_id', back_populates="reservations")
    actual_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)

    ### CONSTANTS ####
    MAX_TIME_RESERVATION = 3

    def __init__(self, user, table, start_time, end_time=None):
        self.user = user
        self.table = table
        self.start_time = start_time
        # end_time will be set automatically as start_time + 3 hours
        self.end_time = start_time + timedelta(hours=self.MAX_TIME_RESERVATION)
        # TODO: change the 3 with a constant0

    def set_user(self, user):
        self.user = user

    def set_table(self, table):
        self.table = table

    def set_start_time(self, start_time):
        self.actual_time = datetime.datetime.now()
        print(self.actual_time)
        if start_time > self.actual_time:
            self.start_time = start_time
        else:
            raise ValueError("Invalid reservation start time")
    
    def get_end_time(self):
        return self.__end_time
    
    def set_end_time(self, end_time):
        self.__end_time = end_time

    def set_is_active(self, is_active):
        self.is_active = is_active
