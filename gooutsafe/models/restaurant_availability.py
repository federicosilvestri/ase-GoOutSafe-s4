from sqlalchemy.orm import relationship

from gooutsafe import db


class RestaurantAvailability(db.Model):
    __tablename__ = 'RestaurantAvailability'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("Restaurant.id", ondelete="CASCADE"))
    restaurant = relationship("Restaurant", back_populates="availabilities")

    def __init__(self, restaurant_id, start_time, end_time):
        self.restaurant_id = restaurant_id
        self.start_time = start_time
        self.end_time = end_time

    def set_times(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
