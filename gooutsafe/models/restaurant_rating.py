from gooutsafe import db


class RestaurantRating(db.Model):
    MIN_VALUE = 0
    MAX_VALUE = 10

    __tablename__ = 'RestaurantRating'

    REVIEW_MAX_LENGTH = 200

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey('Customer.id'),
        primary_key=True
    )

    restaurant_id = db.Column(
        db.Integer,
        db.ForeignKey('Restaurant.id'),
        primary_key=True
    )

    value = db.Column(
        db.SmallInteger,
    )

    review = db.Column(
        db.Text(
            length=REVIEW_MAX_LENGTH,
        ),
        nullable=True
    )

    def __init__(self, customer_id, restaurant_id, value: int, review=None):
        self.customer_id = customer_id
        self.restaurant_id = restaurant_id
        self.value = value
        self.review = review

    @staticmethod
    def check_value(value: int):
        if value < RestaurantRating.MIN_VALUE or value > RestaurantRating.MAX_VALUE:
            raise ValueError('Invalid value for rating!')

    @staticmethod
    def check_review(review: str):
        if len(review) > RestaurantRating.MAX_VALUE:
            raise ValueError('Review\'s length must not be greater than MAX_SIZE')

    def set_value(self, value):
        RestaurantRating.check_value(value)
        self.value = value

    def set_review(self, review):
        RestaurantRating.check_review(review)
        self.review = review






