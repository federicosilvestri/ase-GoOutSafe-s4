from gooutsafe import db
from .user import User


class Customer(User):
    __tablename__ = 'Customer'

<<<<<<< HEAD
    __id = db.Column(db.Integer, db.ForeignKey('User.__id'), primary_key=True)
    __firstname = db.Column(db.Unicode(128))
    __lastname = db.Column(db.Unicode(128))
    __date_of_birth = db.Column(db.DateTime)
    __health_status = db.Column(db.Boolean, default=False)
=======
    id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)
    firstname = db.Column(db.Unicode(128))
    lastname = db.Column(db.Unicode(128))
    birthday = db.Column(db.DateTime)
    health_status = db.Column(db.Boolean, default=False)
>>>>>>> a3d7a2792655935ded85d6573efabb59ec9b3abd

    __mapper_args__ = {
        'polymorphic_identity': 'customer',
    }

    def __init__(self, *args, **kw):
        super(Customer, self).__init__(*args, **kw)
        self._authenticated = False

    def set_firstname(self, name):
        self.firstname = name

    def set_lastname(self, name):
        self.lastname = name

    def set_birthday(self, birthday):
        self.birthday = birthday

    def set_health_status(self, status):
        self.health_status = status
