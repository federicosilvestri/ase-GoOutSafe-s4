from .user import User

from gooutsafe import db


class Customer(User):
    __tablename__ = 'Customer'

    firstname = db.Column(db.Unicode(128))
    lastname = db.Column(db.Unicode(128))
    date_of_birth = db.Column(db.DateTime)
    health_status = db.Column(db.Boolean, default=False)

    def __init__(self, *args, **kw):
        super(User, self).__init__(*args, **kw)
        self._authenticated = False

    @property
    def firstname(self):
        return self.firstname

    @firstname.setter
    def firstname(self, name):
        self.firstname = name

    @property
    def lastname(self):
        return self.lastname

    @lastname.setter
    def lastname(self, name):
        self.lastname = name

    @property
    def date_of_birth(self):
        return self.date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, dateBirth):
        self.date_of_birth = dateBirth

    @property
    def health_status(self):
        return self.health_status

    @health_status.setter
    def health_status(self, status):
        self.health_status = status
