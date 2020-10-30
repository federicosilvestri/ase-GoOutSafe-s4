from flask import Blueprint, redirect, render_template, request
from flask_login import login_required
from gooutsafe import db
from gooutsafe.auth import current_user
from gooutsafe.models.restaurant import Restaurant
from gooutsafe.models.reservation import Reservation
from gooutsafe.dao.reservation_manager import ReservationManager
from gooutsafe.dao.restaurant_manager import RestaurantManager
from gooutsafe.forms.reservation import ReservationForm

reservation = Blueprint('reservation', __name__)

#TODO: only customer can create a new reservation
@reservation.route('/create_reservation/<restaurant_id>', methods=['GET', 'POST'])
@login_required
def create_reservation(restaurant_id):
    form = ReservationForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = current_user
            #table=
            restuarant = RestaurantManager.retrieve_by_id(restaurant_id)
            start_data = form.data['start_date']
            start_time = form.data['start_time']
            people_number = form.data['people_number']
            reservation = Reservation(user, table, restaurant, people_number, start_data)
            ReservationManager.create_reservation(reservation)

            return redirect('/reservations/' + str(restaurant_id) + '/' + str(reservation.id))

    return render_template('create_reservation.html', form=form)


@reservation.route('<restaurant_id>/delete_reservation/<int:id>')
def delete_reservation():
    #TODO: implement this method
    pass

@reservation.route('reservations/<restaurant_id>/<reservation_id>')
def reservation_details(restaurant_id, reservation_id):
    reservation = db.session.query(Reservation).filter_by(id=int(reservation_id)).all()[0]
    user = reservatio.user
    table = reservation.table
    restaurant = reservation.restaurant
    return render_template("reservation_details.html", reservation = reservation, user = user, table = table, restaurant = restaurant)