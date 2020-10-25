from sqlalchemy.orm import relationship

from gooutsafe import db


class Like(db.Model):
    __tablename__ = 'Like'

    liker_id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)
    liker = relationship('User', foreign_keys='Like.liker_id')

    restaurant_id = db.Column(db.Integer, db.ForeignKey('Restaurant.id'), primary_key=True)
    restaurant = relationship('Restaurant', foreign_keys='Like.restaurant_id')

    marked = db.Column(db.Boolean, default=False)  # True iff it has been counted in Restaurant.likes
