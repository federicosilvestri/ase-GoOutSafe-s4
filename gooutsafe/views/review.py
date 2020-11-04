from flask import Blueprint, render_template, redirect, request
from flask_login import (login_required, current_user)
from gooutsafe.forms.review import ReviewForm
from gooutsafe.models.restaurant_rating import RestaurantRating
from gooutsafe.dao.restaurant_rating_manager import RestaurantRatingManager

review = Blueprint('review', __name__)


@review.route('/restaurants/<int:restaurant_id>/review', methods=['GET', 'POST'])
@login_required
def write_review(restaurant_id):
    form = ReviewForm()

    if RestaurantRatingManager.check_existence(restaurant_id, current_user.id):
        return render_template('thank_you_review.html', already_written=True, restaurant_id=restaurant_id)

    if request.method == 'GET':
        return render_template('create_review.html', form=form, rating_min_value=RestaurantRating.MIN_VALUE,
                               rating_max_value=RestaurantRating.MAX_VALUE)
    else:
        if form.is_submitted():
            rest_rating = RestaurantRating(
                current_user.id,
                restaurant_id,
                form.data['value'],
                form.data['review']
            )

            RestaurantRatingManager.create_rating(rest_rating)
        return render_template('thank_you_review.html', restaurant_id=restaurant_id)

