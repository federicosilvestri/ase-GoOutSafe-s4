from flask import Blueprint, render_template
from flask_login import login_required
from gooutsafe import db
from gooutsafe.auth import current_user
from gooutsafe.models.restaurant import Restaurant
from gooutsafe.models.reservation import Reservation
from gooutsafe.dao.reservation_manager import ReservationManager

reservation = Blueprint('reservation', __name__)

#TODO: only customer can create a new reservation
@reservation.route('/create_reservation/<id>', methods=['GET', 'POST'])
@login_required
def create_reservation(id):
    
    return render_template("create_reservation.html")

@reservation.route('<restaurant_id>/delete_reservation/<int:id>')
def delete_reservation():
    #TODO: implement this method
    pass

@reservation.route('<restaurant_id>/reservations/<reservation_id>')
def reservation_details(reservation_id):
    reservation = db.session.query(Reservation).filter_by(id=int(reservation_id)).all()[0]
    user = reservatio.user
    table = reservation.table
    restaurant = reservation.restaurant
    return render_template("reservation_details.html", reservation = reservation, user = user, table = table, restaurant = restaurant)