from sqlalchemy.orm import relationship
from datetime import timedelta
from datetime import datetime

from gooutsafe import db


class Reservation(db.Model):
    __tablename__ = 'Reservation'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    user = relationship('User', foreign_keys='Reservation.user_id')
    table_id = db.Column(db.Integer, db.ForeignKey('Table.id'))
    table = relationship('Table', foreign_keys='Reservation.table_id', back_populates="reservations")
    actual_time = db.Column(db.DateTime)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)

    def __init__(self, user, table, start_time, is_active=True, end_time=None):
        self.user = user
        self.table = table
        self.actual_time = datetime.now()
        self.start_time = start_time
        # end_time will be set automatically as start_time + 3 hours
        self.end_time = start_time + timedelta(hours=3)
        #TODO: change the 3 with a constant

    @property
    def user(self):
        return self.__user
    
    @user.setter
    def user(self, user):
        self.__user = user

    @property
    def table(self):
        return self.__table
    
    @table.setter
    def table(self, table):
        self.__table = table

    @property
    def actual_time(self):
        return self.__actual_time

    @property
    def start_time(self):
        return self.__start_time
    
    @start_time.setter
    def start_time(self, start_time):
        if(start_time > actual_time):
            self.__start_time = start_time
        else:
            raise ValueError("Invalid reservation start time")
    
    @property
    def end_time(self):
        return self.__end_time
    
    @end_time.setter
    def table(self, end_time):
        self.__end_time = end_time

    @property
    def is_active(self):
        return self.__is_active
    
    @is_active.setter
    def is_active(self, is_active):
        self.__is_active = is_active