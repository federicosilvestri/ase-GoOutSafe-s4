from flask import Blueprint, render_template

from gooutsafe import db
from gooutsafe.auth import current_user
from gooutsafe.models.restaurant import Restaurant
from gooutsafe.models.reservation import Reservation

reservation = Blueprint('reservation', __name__)


@reservation.route('/reservation/create_reservation')
def create_reservation():
    #TODO: implement this method
    pass

@reservation.route('/reservations/<reservation_id>')
def reservation_details(reservation_id):
    reservation = db.session.query(Reservation).filter_by(id=int(reservation_id)).all()[0]
    user_email = reservation.user.email
    table = reservation.table
    start_time = reservation.start_time
    return render_template("reservation_details.html", user = name, table = table, start_time = start_time)