from datetime import datetime
from datetime import timedelta

from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import login_required

# from flask_user import roles_required
from gooutsafe.auth import current_user
from gooutsafe.dao.customer_manager import CustomerManager
from gooutsafe.dao.reservation_manager import ReservationManager
from gooutsafe.dao.restaurant_manager import RestaurantManager
from gooutsafe.dao.table_manager import TableManager
from gooutsafe.forms.filter_form import FilterForm
from gooutsafe.forms.reservation import ReservationForm
from gooutsafe.models.reservation import Reservation
from gooutsafe.models.restaurant import Restaurant
from gooutsafe.models.table import Table

reservation = Blueprint('reservation', __name__)


# TODO: only customer can create a new reservation
@reservation.route('/create_reservation/<restaurant_id>', methods=['GET', 'POST'])
@login_required
# @roles_required('customer')
def create_reservation(restaurant_id):
    form = ReservationForm()
    restaurant = RestaurantManager.retrieve_by_id(restaurant_id)
    if request.method == 'POST':
        if form.validate_on_submit():
            start_data = form.data['start_date']
            start_time = form.data['start_time']
            people_number = form.data['people_number']
            start_time_merged = datetime.combine(start_data, start_time)
            table = validate_reservation(restaurant, start_time_merged, people_number)
            if table != False:
                reservation = Reservation(current_user, table, restaurant, people_number, start_time_merged)
                ReservationManager.create_reservation(reservation)
                return redirect(url_for('reservation.reservation_details',
                                        restaurant_id=restaurant_id, reservation_id=reservation.id))
            else:
                flash("There aren't free tables for that hour or the restaurant is close")
    return render_template('create_reservation.html', restaurant=restaurant, form=form)


def validate_reservation(restaurant, start_datetime, people_number):
    """
    This method checks if the new reservation overlap with other already 
    present for the restaurant.
    Args:
        restaurant (Restaurant): the reservation restaurant
        start_datetime (datetime): the datetime of the reservation
        people_number (Integer): number of people declered in the reservation

    Returns:
        Teble, Boolean: false in case there are overlap or a table if the restaurant is open and there aren't overlap
    """
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
                            if check_time_interval(start_datetime.time(), end_datetime.time(),
                                                   old_start_datetime.time(), old_end_datetime.time()):
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
    """
    This method check if the reservation datetime fall in the retaurant opening hours
    
    Args:
        restaurant (Restaurant): the restaurant in whitch we are booking
        start_datetime (datetime): reservation datetime 
        end_datetime (datetime): reservation end datetime

    Returns:
        [Boolean]: True if the restaurant is open or False if the restaurant is close
    """
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
def delete_reservation(id, restaurant_id):
    ReservationManager.delete_reservation_by_id(id)
    return redirect(url_for('reservation.reservation_all', restaurant_id=restaurant.id))


@reservation.route('/reservations/<restaurant_id>/<reservation_id>', methods=['GET', 'POST'])
def reservation_details(restaurant_id, reservation_id):
    reservation = ReservationManager.retrieve_by_id(reservation_id)
    user = CustomerManager.retrieve_by_id(reservation.user.id)
    table = reservation.table
    restaurant = reservation.restaurant
    return render_template("reservation_details.html", reservation=reservation,
                           user=user, table=table, restaurant=restaurant)


@reservation.route('/reservations/<restaurant_id>', methods=['GET', 'POST'])
def reservation_all(restaurant_id):
    """Returns the whole list of reservations, given a restaurant.
    It also gives to the operator the opportunity to filter reservations
    by date, so it's possible to count people.

    Returns:
        The template of the reservations.
    """
    filter_form = FilterForm()
    reservations = ReservationManager.retrieve_by_restaurant_id(restaurant_id)
    restaurant = RestaurantManager.retrieve_by_id(restaurant_id)
    people = 0
    for r in reservations:
        people = people + r.people_number

    if request.method == 'POST':
        if filter_form.is_submitted():
            filter_date = filter_form.data['filter_date']
            start_time = filter_form.data['start_time']
            end_time = filter_form.data['end_time']

            if filter_date is not None and start_time is not None and end_time is not None:
                start_date_time = datetime.combine(filter_date, start_time)
                end_date_time = datetime.combine(filter_date, end_time)
                res = ReservationManager.retrieve_by_date_and_time(
                    restaurant_id, start_date_time, end_date_time
                )
                people = 0
                for r in res:
                    people = people + r.people_number

                return render_template("restaurant_reservation.html",
                                       restaurant=restaurant, reservations=res,
                                       filter_form=filter_form, people=people)
            else:
                flash("The form is not correct")

    return render_template("restaurant_reservation.html",
                           restaurant=restaurant, reservations=reservations,
                           filter_form=filter_form, people=people)


@reservation.route('/delete/<int:id>/<int:customer_id>', methods=['GET', 'POST'])
def delete_reservation_customer(id, customer_id):
    """Given a customer and a reservation id,
    this function delete the reservation from the database.

    Returns:
        Redirects the view to the customer profile page.
    """
    ReservationManager.delete_reservation_by_id(id)
    return redirect(url_for('auth.profile', id=id))


@reservation.route('/edit/<int:reservation_id>/<int:customer_id>', methods=['GET', 'POST'])
def edit_reservation(reservation_id, customer_id):
    """Allows the customer to edit a single reservation,
    if there's an available table within the opening hours
    of the restaurant.

    Returns:
        Redirects the view to the customer profile page.
    """
    form = ReservationForm()
    reservation = ReservationManager.retrieve_by_customer_id(user_id=customer_id)[0]
    restaurant = RestaurantManager.retrieve_by_id(reservation.restaurant_id)

    if request.method == 'POST':
        if form.validate_on_submit():
            start_data = form.data['start_date']
            start_time = form.data['start_time']
            people_number = form.data['people_number']
            start_time_merged = datetime.combine(start_data, start_time)
            table = validate_reservation(restaurant, start_time_merged, people_number)
            if table != False:
                reservation.set_people_number(people_number)
                reservation.set_start_time(start_time_merged)
                reservation.set_table(table)
                ReservationManager.update_reservation(reservation)
            else:
                flash("There aren't free tables for that hour or the restaurant is close")
        else:
            flash("The form is not correct")

    return redirect(url_for('auth.profile', id=customer_id))
