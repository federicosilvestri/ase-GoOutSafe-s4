from flask import Blueprint, redirect, render_template, request
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
    restaurant = RestaurantManager.retrieve_by_id(restaurant_id)
    time_slots_avail = get_time_slots(restaurant)
    form = ReservationForm(time_slots_avail)
    if request.method == 'POST':
        if form.is_submitted():
            start_data = form.data['start_date']
            print(start_data)
            start_time = form.data['time_slots']
            merged_str_datetime = str(start_data) + ' ' + str(start_time)
            print(merged_str_datetime)
            merged_start_datetime = datetime.strptime(merged_str_datetime, '%Y-%m-%d %H:%M')
            print(merged_start_datetime)
            people_number = form.data['people_number']
            table = get_free_table(restaurant,people_number)
            reservation = Reservation(current_user, table, restaurant, people_number, merged_start_datetime)
            ReservationManager.create_reservation(reservation)
            return redirect('/reservations/' + str(restaurant_id) + '/' + str(reservation.id)) 
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


def check_time_slot(new_start_datetime, restaurant):
    rest_reservations = ReservationManager.retrieve_by_restaurant_id(restaurant.restaurant_id)
    new_end_datetime = new_end_datetime + timedelta(hours=Reservation.MAX_TIME_RESERVATION)
    for rest_res in rest_reservations:
        if (new_start_datetime > rest_res.start_time or new_start_datetime < rest_res.end_datetime) or (new_end_datetime > rest_res.start_time or new_end_datetime < rest_res.end_datetime):
            return False
    return True


@reservation.route('/<restaurant_id>/delete_reservation/<int:id>')
def delete_reservation(restaurant_id, id):
    #TODO: implement this method
    pass

@reservation.route('/reservations/<restaurant_id>/<reservation_id>')
def reservation_details(restaurant_id, reservation_id):
    reservation = ReservationManager.retrieve_by_id(reservation_id)
    user = CustomerManager.retrieve_by_id(reservation.user.id)
    print(user.firstname)
    table = reservation.table
    restaurant = reservation.restaurant
    return render_template("reservation_details.html", reservation = reservation, user = user, table = table, restaurant = restaurant)