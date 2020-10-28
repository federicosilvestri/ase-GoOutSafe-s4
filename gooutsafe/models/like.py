from sqlalchemy.orm import relationship
import datetime

from gooutsafe import db


class Like(db.Model):
    __tablename__ = 'Like'

    liker_id = db.Column(db.Integer, db.ForeignKey('User.id', ondelete="CASCADE"),  
                    primary_key=True)
    liker = relationship('User', foreign_keys='Like.liker_id')

    restaurant_id = db.Column(db.Integer, db.ForeignKey('Restaurant.id', ondelete="CASCADE"), 
                    primary_key=True)
    restaurant = relationship('Restaurant', foreign_keys='Like.restaurant_id')

    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, *args, **kw):
        super(Like, self).__init__(*args, **kw)


