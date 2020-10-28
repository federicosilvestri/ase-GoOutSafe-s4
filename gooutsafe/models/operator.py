from gooutsafe import db
from .user import User
from sqlalchemy.orm import relationship


class Operator(User):
    __tablename__ = 'Operator'

<<<<<<< HEAD
    id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('Restaurant.id'))
    restaurant = relationship('Restaurant', back_populates="operator")
=======
    id = db.Column(db.Integer, db.ForeignKey('User.id', ondelete='CASCADE'), primary_key=True)
    restaurant = relationship('Restaurant', uselist=False, back_populates="owner")
>>>>>>> 8e25b93769f2fce48e59cade2f7dc807bc1c1bba

    __mapper_args__ = {
        'polymorphic_identity': 'operator',
    }

    def __init__(self, *args, **kw):
        super(Operator, self).__init__(*args, **kw)
        self._authenticated = False
        
