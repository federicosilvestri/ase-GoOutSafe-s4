from gooutsafe import db
from .user import User


class Operator(User):
    __tablename__ = 'Operator'

<<<<<<< HEAD
    _id = db.Column(db.Integer, db.ForeignKey('User.__id'), primary_key=True)
=======
    id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)
>>>>>>> a3d7a2792655935ded85d6573efabb59ec9b3abd

    __mapper_args__ = {
        'polymorphic_identity': 'operator',
    }

    def __init__(self, *args, **kw):
        super(Operator, self).__init__(*args, **kw)
        self._authenticated = False

    def get_id(self):
        return self.id
