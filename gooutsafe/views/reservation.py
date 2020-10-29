from flask import Blueprint, render_template

from gooutsafe import db
from gooutsafe.auth import current_user
from gooutsafe.models.restaurant import Restaurant
from gooutsafe.models.reservation import Reservation
from gooutsafe.dao.reservation_manager import Reservation_Manager

reservation = Blueprint('reservation', __name__)


@reservation.route('/reservation/create_reservation')
def create_reservation():
    #TODO: implement this method
    pass

@reservation.route('/delete_reservation/<int:id>')
def delete_reservation():
    #TODO: implement this method
    pass

@reservation.route('/reservations/<reservation_id>')
def reservation_details(reservation_id):
    reservation = db.session.query(Reservation).filter_by(id=int(reservation_id)).all()[0]
    user = reservatio.user
    table = reservation.table
    restaurant = reservation.restaurant
    return render_template("reservation_details.html", reservation = reservation, user = user, table = table, restaurant = restaurant)