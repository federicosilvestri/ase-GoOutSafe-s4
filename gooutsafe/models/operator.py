from werkzeug.security import generate_password_hash, check_password_hash
from .user import User

from gooutsafe import db


class Operator(User):
    __tablename__ = 'Operator'

    id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity':'operator',
    }

    def __init__(self, *args, **kw):
        super(Operator, self).__init__(*args, **kw)
        self._authenticated = False

    def get_id(self):
        return self.id