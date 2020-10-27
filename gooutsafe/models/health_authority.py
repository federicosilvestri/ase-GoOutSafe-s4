from gooutsafe import db
from .user import User


class Authority(User):
    __tablename__ = 'Authority'

<<<<<<< HEAD
    __id = db.Column(db.Integer, db.ForeignKey('User.__id'), primary_key=True)
    __name = db.Column(db.Unicode(128))
    __city = db.Column(db.Unicode(128))
    __address = db.Column(db.Unicode(128))
    __phone = db.Column(db.Unicode(128))
=======
    id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)
    name = db.Column(db.Unicode(128))
    city = db.Column(db.Unicode(128))
    address = db.Column(db.Unicode(128))
    phone = db.Column(db.Unicode(128))
>>>>>>> a3d7a2792655935ded85d6573efabb59ec9b3abd

    __mapper_args__ = {
        'polymorphic_identity': 'authority',
    }

    def __init__(self, *args, **kw):
        super(Authority, self).__init__(*args, **kw)
        self._authenticated = False
