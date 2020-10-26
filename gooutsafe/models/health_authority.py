from .user import User

from gooutsafe import db


class Authority(User):
    __tablename__ = 'Authority'

    id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)
    name = db.Column(db.Unicode(128))
    city = db.Column(db.Unicode(128))
    address = db.Column(db.Unicode(128))
    phone = db.Column(db.Unicode(128))

    __mapper_args__ = {
        'polymorphic_identity':'authority',
    }

    def __init__(self, *args, **kw):
        super(Authority, self).__init__(*args, **kw)
        self._authenticated = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone