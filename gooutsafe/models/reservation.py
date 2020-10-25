from sqlalchemy.orm import relationship

from gooutsafe import db


class Reservation(db.Model):
    __tablename__ = 'Reservation'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    user = relationship('User', foreign_keys='Reservation.user_id')
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'))
    table = relationship('Table', foreign_keys='Table.table_id', back_populates="Reservations")
    timestamp = db.Column(db.DateTime)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)

    def __init__(self, user, table, timestamp, start_time, active=True, end_time=None):
        self.user = user
        self.table = table
        self.timestamp = timestamp
        self.start_time = start_time
        """
        end_time will be set automatically as start_time + 3 hours
        """
        self.end_time = start_time + 10800

    
