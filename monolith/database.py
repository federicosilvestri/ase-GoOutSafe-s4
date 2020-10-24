from werkzeug.security import generate_password_hash, check_password_hash
import enum
from sqlalchemy.orm import relationship
import datetime as dt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Unicode(128), nullable=False)
    firstname = db.Column(db.Unicode(128))
    lastname = db.Column(db.Unicode(128))
    password = db.Column(db.Unicode(128))
    dateofbirth = db.Column(db.DateTime)
    role = db.Column(db.Unicode(128))
    is_active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=False)
    is_anonymous = False

    def __init__(self, *args, **kw):
        super(User, self).__init__(*args, **kw)
        self._authenticated = False

    def set_password(self, password):
        self.password = generate_password_hash(password)

    @property
    def is_authenticated(self):
        return self._authenticated

    def authenticate(self, password):
        checked = check_password_hash(self.password, password)
        self._authenticated = checked
        return self._authenticated

    def get_id(self):
        return self.id


class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text(100)) 
    
    likes = db.Column(db.Integer) # will store the number of likes, periodically updated in background

    lat = db.Column(db.Float) # restaurant latitude
    lon = db.Column(db.Float) # restaurant longitude

    phone = db.Column(db.Integer)


class Like(db.Model):
    __tablename__ = 'like'
    
    liker_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    liker = relationship('User', foreign_keys='Like.liker_id')

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), primary_key=True)
    restaurant = relationship('Restaurant', foreign_keys='Like.restaurant_id')

    marked = db.Column(db.Boolean, default = False) # True iff it has been counted in Restaurant.likes 

class Table(db.Model):
    __tablename__= 'Table'

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    resturant_id = relationship('rRsturant', foreign_keys='resturant.resturant_id')
    capacity = db.Column(db.Integer)

    def __init__(self, id, capacity, resturant):
        self.id = id
        self.capacity = capacity
        self.resturant = resturant

    

class Reservation(db.Model):
    __tablename__ = 'Reservation'

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)
    user = relationship('User', foreign_keys='Reservation.user_id')
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'))
    table = relationship('Table', foreign_keys='Table.table_id')
    timestamp = db.Column(db.DataTime)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)

    def __init__(self, user, table, timestamp, start_time, active = True, end_time = None):
        self.user = user
        self.table = table
        self.timestamp = timestamp
        self.start_time = start_time
        #Automatically end_time will be set as start_time + 3 hours
        self.end_time =  start_time + 10800


    def setActiveToFalse(self):
        self.active = False

    def isActive(self):
        return self.active
