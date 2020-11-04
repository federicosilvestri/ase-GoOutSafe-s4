import wtforms as f
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, NumberRange

from gooutsafe.models.restaurant_rating import RestaurantRating


class ReviewForm(FlaskForm):
    value = f.IntegerField(
        'Rate',
        validators=[NumberRange(
            min=RestaurantRating.MIN_VALUE,
            max=RestaurantRating.MAX_VALUE
        )]
    )

    review = f.TextAreaField(
        'Review',
        validators=[DataRequired()]
    )
