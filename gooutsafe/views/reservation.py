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
    form = ReservationForm()
    restaurant = RestaurantManager.retrieve_by_id(restaurant_id)
    if request.method == 'POST':
        if form.is_submitted():
            start_data = form.data['start_date']
            start_time = form.data['start_time']
            people_number = form.data['people_number']
            start_time_merged = datetime.combine(start_data, start_time)
            print(str(start_time_merged))
            table = validate_reservation(restaurant, start_time_merged, people_number)
            if table != False:
                reservation = Reservation(current_user, table, restaurant, people_number, start_time_merged)
                ReservationManager.create_reservation(reservation)
                return redirect('/reservations/' + str(restaurant_id) + '/' + str(reservation.id)) 
            else:
                print("#######################################")
    return render_template('create_reservation.html', restaurant=restaurant, form=form)


def validate_reservation(restaurant, start_datetime, people_number):
    end_datetime = start_datetime + timedelta(hours=Reservation.MAX_TIME_RESERVATION)
    if check_rest_ava(restaurant, start_datetime, end_datetime):
        print('RISTORANTE APERTO')
        tables = TableManager.retrieve_by_restaurant_id(restaurant.id).order_by(Table.capacity)
        reservation_table = None
        for table in tables:
            print('RICERCA TAVOLO')
            if table.capacity >= people_number:
                print('TAVOLO ADATTO')
                reservation_table = table
                table_reservations = ReservationManager.retrieve_by_table_id(table_id=table.id)
                if len(table_reservations) != 0:
                    print('\nRICERCA OVERLAP\n')
                    for r in table_reservations:
                        old_start_datetime = r.start_time
                        old_end_datetime = r.end_time
                        print(old_start_datetime)
                        print(old_end_datetime)
                        if start_datetime.date() == old_start_datetime.date():
                            print('OVERLAP DATA\n')
                            if check_time_interval(start_datetime.time(), end_datetime.time(), old_start_datetime.time(), old_end_datetime.time()):
                                print('OVERLAP PRENOTAZIONI')
                                pass
                            else:
                                print('NON CI SONO PRENOTAZIONI - TAVOLO DISPONIBILE')
                                return reservation_table
                        else:
                            print('NON CI SONO PRENOTAZIONI - TAVOLO DISPONIBILE')
                            return reservation_table
                else:
                    print('NON CI SONO PRENOTAZIONI - TAVOLO DISPONIBILE')
                    return reservation_table
            else:
                print('NON CI SONO TAVOLI DISPONIBILE')
                return False
    return False

def check_rest_ava(restaurant, start_datetime, end_datetime):
    availabilities = restaurant.availabilities
    for ava in availabilities:
        print(ava.start_time)
        print(ava.end_time)
        if check_time_interval(start_datetime.time(), end_datetime.time(), ava.start_time, ava.end_time):
            return True
        print('RISTORANTE CHIUSO')
    return False

        
def check_time_interval(start_time1, end_time1, start_time2, end_time2):
    """
    This method check if start_time1 and end_time1 overlap
    the intervall between startime2 and end_time2

    Args:
        start_time1 (datetime): [description]
        end_time1 (datetime): [description]
        start_time2 (datetime): [description]
        end_time2 (datetime): [description]

    Returns:
        Boolean: [description]
    """
    if start_time1 >= start_time2 and start_time1 < end_time2:
        print('***OVERLAP 1***')
        return True
    elif end_time1 > start_time2 and end_time1 <= end_time2:
        print('***OVERLAP 2***')
        return True
    return False
    

@reservation.route('/delete/<int:id>/<restaurant_id>')
def delete_reservation(restaurant_id, id):
    ReservationManager.delete_reservation_by_id(id)
    return redirect ('/reservations/'+ str(restaurant_id))


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