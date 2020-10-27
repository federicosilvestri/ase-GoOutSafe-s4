from datetime import timedelta
from datetime import datetime

from sqlalchemy.orm import relationship

from gooutsafe import db


class Reservation(db.Model):
    __tablename__ = 'Reservation'

    __id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    __user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    __user = relationship('User', foreign_keys='Reservation.user_id')
    __table_id = db.Column(db.Integer, db.ForeignKey('Table.id'))
    __table = relationship('Table', foreign_keys='Reservation.table_id', back_populates="reservations")
    __actual_time = db.Column(db.DateTime)
    __start_time = db.Column(db.DateTime)
    __end_time = db.Column(db.DateTime)

    ### CONSTANTS ####
    MAX_TIME_RESERVATION = 3


    def __init__(self, user, table, start_time, is_active=True, end_time=None):
        self.__user = user
        self.__table = table
        Reservation.actual_time = datetime.now()       
        self.__start_time = start_time
        # end_time will be set automatically as start_time + 3 hours
        Reservation.__end_time = start_time + timedelta(hours=self.MAX_TIME_RESERVATION)
        #TODO: change the 3 with a constant0


    def get_id(self):
        return self.__id

    def get_user(self):
        return self.__user

    def set_user(self, user):
        self.__user = user

    def get_table(self):
        return self.__table
  
    def set_table(self, table):
        self.__table = table

    def get_actual_time(self):
        return self.__actual_time

    def get_start_time(self):
        return self.__start_time
    
    def set_start_time(self, start_time):
        if(start_time > self.actual_time):
            self.__start_time = start_time
        else:
            raise ValueError("Invalid reservation start time")
    
    def get_end_time(self):
        return self.__end_time
    
    def set_table(self, end_time):
        self.__end_time = end_time

    def get_is_active(self):
        return self.__is_active
    
    def set_is_active(self, is_active):
        self.__is_active = is_active
