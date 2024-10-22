from sqlalchemy.orm import relationship

from gooutsafe import db


class RestaurantAvailability(db.Model):
    __tablename__ = 'RestaurantAvailability'

    MAX_DAY_LENGTH = 10

    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    day = db.Column(db.String(length=MAX_DAY_LENGTH))
    restaurant_id = db.Column(db.Integer, db.ForeignKey("Restaurant.id", ondelete="CASCADE"))
    restaurant = relationship("Restaurant", back_populates="availabilities")

    def __init__(self, restaurant_id, day, start_time, end_time):
        self.restaurant_id = restaurant_id
        self.set_day(day)
        self.start_time = start_time
        self.end_time = end_time

    def set_times(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def set_day(self, day):
        day = day.title()
        if day in self.week_days:
            self.day = day
        else:
            raise ('The string must be one of the week days')
