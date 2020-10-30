from sqlalchemy.orm import relationship

from gooutsafe import db


class RestaurantAvailability(db.Model):
    __tablename__ = 'RestaurantAvailability'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("Restaurant.id", ondelete="CASCADE"))
    restaurant = relationship("Restaurant", back_populates="availabilities")

    @staticmethod
    def __check_times(start_time, end_time):
        if start_time >= end_time:
            raise ValueError('End time must be greater than start time! (%s >= %s)' % (start_time, end_time))

    def __init__(self, restaurant_id, start_time, end_time):
        RestaurantAvailability.__check_times(start_time, end_time)

        self.restaurant_id = restaurant_id
        self.start_time = start_time
        self.end_time = end_time

    def set_times(self, start_time, end_time):
        RestaurantAvailability.__check_times(start_time, end_time)
        self.start_time = start_time
        self.end_time = end_time
