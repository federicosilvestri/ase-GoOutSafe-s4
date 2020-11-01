from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required
#from flask_user import roles_required
from gooutsafe import db
from gooutsafe.auth import current_user

from gooutsafe.models.restaurant import Restaurant
from gooutsafe.models.reservation import Reservation
from gooutsafe.models.restaurant_availability import RestaurantAvailability
from gooutsafe.models.table import Table

from gooutsafe.dao.reservation_manager import ReservationManager
from gooutsafe.dao.restaurant_manager import RestaurantManager
from gooutsafe.dao.customer_manager import CustomerManager
from gooutsafe.dao.table_manager import TableManager

from gooutsafe.forms.reservation import ReservationForm

from datetime import time
from datetime import datetime
from datetime import timedelta

reservation = Blueprint('reservation', __name__)

#TODO: only customer can create a new reservation
@reservation.route('/create_reservation/<restaurant_id>', methods=['GET', 'POST'])
@login_required
#@roles_required('customer')
def create_reservation(restaurant_id):
    form = ReservationForm()
    restaurant = RestaurantManager.retrieve_by_id(restaurant_id)
    if request.method == 'POST':
        if form.is_submitted():
            start_data = form.data['start_date']
            print(start_data)
            start_time = form.data['start_time']
            print(start_time)
            people_number = form.data['people_number']
            print(people_number)
            table = get_free_table(restaurant,people_number)
            start_time = datetime.combine(start_data, start_time)
            reservation = Reservation(current_user, table, restaurant, people_number, start_time)
            ReservationManager.create_reservation(reservation)
            return redirect(url_for('reservation.reservation_details',
                    restaurant_id=restaurant_id, reservation_id=reservation.id))

    return render_template('create_reservation.html', restaurant=restaurant, form=form)


def get_free_table(restaurant, people_number):
    tables = TableManager.retrieve_by_restaurant_id(restaurant.id).order_by(Table.capacity)
    reservation_table = None
    for table in tables:
        if table.capacity >= people_number:
            reservation_table = table
            break
    return reservation_table

def get_time_slots(restaurant):
    time_slots = restaurant.availabilities
    time_slot = time_slots[0]
    start_time = time_slot.start_time
    end_time = time_slot.end_time
    temp_slot = datetime(2020, 1, 1, start_time.hour, start_time.minute)
    end_datetime = datetime(2020, 1, 1, end_time.hour, end_time.minute)
    free_time_slots = []
    while temp_slot < end_datetime:
        free_time_slots.append(temp_slot.strftime('%H:%M'))
        temp_slot += timedelta(minutes=15)
    return free_time_slots

@reservation.route('/delete/<int:id>/<restaurant_id>')
def delete_reservation(id, restaurant_id):
    ReservationManager.delete_reservation_by_id(id)
    return redirect (url_for('reservation.reservation_all', restaurant_id=restaurant.id))


@reservation.route('/reservations/<restaurant_id>/<reservation_id>', methods=['GET', 'POST'])
def reservation_details(restaurant_id, reservation_id):
    reservation = ReservationManager.retrieve_by_id(reservation_id)
    user = CustomerManager.retrieve_by_id(reservation.user.id)
    table = reservation.table
    restaurant = reservation.restaurant
    return render_template("reservation_details.html", reservation = reservation, 
        user = user, table = table, restaurant = restaurant)


@reservation.route('/reservations/<restaurant_id>', methods=['GET', 'POST'])
def reservation_all(restaurant_id):
    restaurant = RestaurantManager.retrieve_by_id(restaurant_id)
    reservations = ReservationManager.retrieve_by_restaurant_id(restaurant_id)
    
    return render_template("restaurant_reservation.html", 
        restaurant=restaurant, reservations=reservations)


@reservation.route('/delete/<int:id>/<int:customer_id>')
def delete_reservation_customer(id, customer_id):
    ReservationManager.delete_reservation_by_id(id)
    return redirect(url_for('auth.profile', id=user.id))