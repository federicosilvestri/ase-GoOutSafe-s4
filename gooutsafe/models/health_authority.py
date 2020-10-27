from gooutsafe import db
from .user import User


class Authority(User):
    __tablename__ = 'Authority'

    __id = db.Column(db.Integer, db.ForeignKey('User.__id'), primary_key=True)
    __name = db.Column(db.Unicode(128))
    __city = db.Column(db.Unicode(128))
    __address = db.Column(db.Unicode(128))
    __phone = db.Column(db.Unicode(128))

    __mapper_args__ = {
        'polymorphic_identity': 'authority',
    }

    def __init__(self, *args, **kw):
        super(Authority, self).__init__(*args, **kw)
        self._authenticated = False

    def get_id (self):
        return self.__id


    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone
