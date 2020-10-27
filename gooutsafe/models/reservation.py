from datetime import timedelta

from sqlalchemy.orm import relationship

from gooutsafe import db


class Reservation(db.Model):
    __tablename__ = 'Reservation'

<<<<<<< HEAD
    __id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    __user_id = db.Column(db.Integer, db.ForeignKey('User.__id'))
    __user = relationship('User', foreign_keys='Reservation.__user_id')
    __table_id = db.Column(db.Integer, db.ForeignKey('Table.__id'))
    __table = relationship('Table', foreign_keys='Reservation.__table_id', back_populates="__reservations")
    __actual_time = db.Column(db.DateTime)
    __start_time = db.Column(db.DateTime)
    __end_time = db.Column(db.DateTime)
=======
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    user = relationship('User', foreign_keys='Reservation.user_id')
    table_id = db.Column(db.Integer, db.ForeignKey('Table.id'))
    table = relationship('Table', foreign_keys='Reservation.table_id', back_populates="reservations")
    actual_time = db.Column(db.DateTime)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
>>>>>>> a3d7a2792655935ded85d6573efabb59ec9b3abd

    ### CONSTANTS ####
    MAX_TIME_RESERVATION = 3

    def __init__(self, user, table, start_time, is_active=True, actual_time=None, end_time=None):
        self.user = user
        self.table = table
        self.actual_time = actual_time
        self.start_time = start_time
        # end_time will be set automatically as start_time + 3 hours
        self.end_time = start_time + timedelta(hours=self.MAX_TIME_RESERVATION)
        # TODO: change the 3 with a constant0

    def set_user(self, user):
        self.user = user

    def set_table(self, table):
        self.table = table

    def set_start_time(self, start_time):
        if start_time > self.actual_time:
            self.start_time = start_time
        else:
            raise ValueError("Invalid reservation start time")
<<<<<<< HEAD
    
    def get_end_time(self):
        return self.__end_time
    
    def set_end_time(self, end_time):
        self.__end_time = end_time
=======

    def set_table(self, end_time):
        self.end_time = end_time
>>>>>>> a3d7a2792655935ded85d6573efabb59ec9b3abd

    def set_is_active(self, is_active):
        self.is_active = is_active
