from sqlalchemy.orm import relationship

from gooutsafe import db


class Like(db.Model):
    __tablename__ = 'Like'

    __liker_id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)
    __liker = relationship('User', foreign_keys='Like.liker_id')

    __restaurant_id = db.Column(db.Integer, db.ForeignKey('Restaurant.id'), primary_key=True)
    __restaurant = relationship('Restaurant', foreign_keys='Like.restaurant_id')

    __marked = db.Column(db.Boolean, default=False)  
            # True iff it has been counted in Restaurant.likes


    def get_liker_id (self):
        return self.__liker_id

    def get_restaurant_id(self):
        return self.__restaurant_id

    def get_marked(self):
        return self.__marked
    
    def set_marked(self, marked):
        self.__marked = marked