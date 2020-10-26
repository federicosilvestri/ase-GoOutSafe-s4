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
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, name):
        self.__firstname = name

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, name):
        self.__lastname = name

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, dateBirth):
        self.__date_of_birth = dateBirth

    @property
    def health_status(self):
        return self.__health_status

    @health_status.setter
    def health_status(self, status):
        self.__health_status = status