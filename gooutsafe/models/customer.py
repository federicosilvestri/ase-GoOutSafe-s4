from gooutsafe import db
from .user import User


class Customer(User):
    __tablename__ = 'Customer'

    __id = db.Column(db.Integer, db.ForeignKey('User.__id'), primary_key=True)
    __firstname = db.Column(db.Unicode(128))
    __lastname = db.Column(db.Unicode(128))
    __date_of_birth = db.Column(db.DateTime)
    __health_status = db.Column(db.Boolean, default=False)

    __mapper_args__ = {
        'polymorphic_identity': 'customer',
    }

    def __init__(self, *args, **kw):
        super(Customer, self).__init__(*args, **kw)
        self._authenticated = False

    
    def get_id(self):
        return self.__id

    def get_firstname(self):
        return self.__firstname

    def set_firstname(self, name):
        self.__firstname = name

    def get_lastname(self):
        return self.__lastname

    def set_lastname(self, name):
        self.__lastname = name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_date_of_birth(self, dateBirth):
        self.__date_of_birth = dateBirth

    def get_health_status(self):
        return self.__health_status

    def set_health_status(self, status):
        self.__health_status = status