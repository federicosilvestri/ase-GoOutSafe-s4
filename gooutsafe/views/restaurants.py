from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import (login_required, current_user)

from gooutsafe import db
from gooutsafe.dao.restaurant_availability_manager import RestaurantAvailabilityManager
from gooutsafe.dao.restaurant_manager import RestaurantManager
from gooutsafe.dao.table_manager import TableManager

from gooutsafe.forms.add_measure import MeasureForm
from gooutsafe.forms.add_table import TableForm
from gooutsafe.forms.add_times import TimesForm
from gooutsafe.forms.restaurant import RestaurantForm
from gooutsafe.forms.filter_form import FilterForm

from gooutsafe.models.restaurant import Restaurant
from gooutsafe.models.restaurant_availability import RestaurantAvailability
from gooutsafe.models.restaurant_rating import RestaurantRating
from gooutsafe.dao.restaurant_rating_manager import RestaurantRatingManager
from gooutsafe.dao.like_manager import LikeManager
from gooutsafe.models.table import Table

restaurants = Blueprint('restaurants', __name__)


@restaurants.route('/restaurants')
def _restaurants(message=''):
    all_restaurants = db.session.query(Restaurant)
    return render_template("restaurants.html", message=message, restaurants=all_restaurants)


@restaurants.route('/restaurants/<restaurant_id>')
@login_required
def restaurant_sheet(restaurant_id):
    restaurant = RestaurantManager.retrieve_by_id(id_=restaurant_id)
    list_measure = restaurant.measures.split(',')
    average_rate = RestaurantRatingManager.calculate_average_rate(restaurant)

    return render_template("restaurantsheet.html",
                           restaurant=restaurant, list_measures=list_measure[1:],
                           average_rate=average_rate, max_rate=RestaurantRating.MAX_VALUE
                           )


@restaurants.route('/restaurants/like/<restaurant_id>')
@login_required
def like_toggle(restaurant_id):
    if LikeManager.like_exists(current_user.id, restaurant_id):
        LikeManager.delete_like(current_user.id, restaurant_id)
    else:
        LikeManager.create_like(current_user.id, restaurant_id)

    return restaurant_sheet(restaurant_id)


@restaurants.route('/restaurants/add/<int:id_op>', methods=['GET', 'POST'])
@login_required
def add(id_op):
    form = RestaurantForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.data['name']
            address = form.data['address']
            city = form.data['city']
            phone = form.data['phone']
            menu_type = form.data['menu_type']
            restaurant = Restaurant(name, address, city, 0, 0, phone, menu_type)
            restaurant.owner_id = id_op

            RestaurantManager.create_restaurant(restaurant)

            return redirect(url_for('auth.operator', id=id_op))

    return render_template('create_restaurant.html', form=form)


@restaurants.route('/restaurants/details/<int:id_op>', methods=['GET', 'POST'])
@login_required
def details(id_op):
    table_form = TableForm()
    time_form = TimesForm()
    measure_form = MeasureForm()
    restaurant = RestaurantManager.retrieve_by_operator_id(id_op)
    list_measure = restaurant.measures.split(',')
    tables = TableManager.retrieve_by_restaurant_id(restaurant.id)
    ava = restaurant.availabilities

    return render_template('add_restaurant_details.html',
                           restaurant=restaurant, tables=tables,
                           table_form=table_form, time_form=time_form,
                           times=ava, measure_form=measure_form, list_measure=list_measure[1:])


@restaurants.route('/restaurants/save/<int:id_op>/<int:rest_id>', methods=['GET', 'POST'])
@login_required
def save_details(id_op, rest_id):
    table_form = TableForm()
    restaurant = RestaurantManager.retrieve_by_operator_id(id_op)

    if request.method == "POST":
        if table_form.is_submitted():
            num_tables = table_form.data['number']
            capacity = table_form.data['max_capacity']

            for i in range(0, num_tables):
                if capacity >= 1:
                    table = Table(capacity=capacity, restaurant=restaurant)
                    TableManager.create_table(table)

    return redirect(url_for('restaurants.details', id_op=id_op))


@restaurants.route('/restaurants/savetime/<int:id_op>/<int:rest_id>', methods=['GET', 'POST'])
@login_required
def save_time(id_op, rest_id):
    time_form = TimesForm()

    if request.method == "POST":
        if time_form.is_submitted():
            start_time = time_form.data['start_time']
            end_time = time_form.data['end_time']

            if end_time > start_time:
                time = RestaurantAvailability(rest_id, start_time, end_time)
                RestaurantAvailabilityManager.create_availability(time)

    return redirect(url_for('restaurants.details', id_op=id_op))


@restaurants.route('/restaurants/savemeasure/<int:id_op>/<int:rest_id>', methods=['GET', 'POST'])
@login_required
def save_measure(id_op, rest_id):
    measure_form = MeasureForm()
    restaurant = RestaurantManager.retrieve_by_operator_id(id_op)

    if request.method == "POST":
        if measure_form.is_submitted():
            list_measure = restaurant.measures.split(',')
            measure = measure_form.data['measure']
            if measure not in list_measure:
                list_measure.append(measure)
            string = ','.join(list_measure)
            restaurant.set_measures(string)
            RestaurantManager.update_restaurant(restaurant)

    return redirect(url_for('restaurants.details', id_op=id_op))


@restaurants.route('/edit_restaurant/<int:id_op>/<int:rest_id>', methods=['GET', 'POST'])
@login_required
def edit_restaurant(id_op, rest_id):
    form = RestaurantForm()
    restaurant = RestaurantManager.retrieve_by_id(rest_id)

    if request.method == "POST":
        if form.is_submitted():
            name = form.data['name']
            restaurant.set_name(name)
            address = form.data['address']
            restaurant.set_address(address)
            city = form.data['city']
            restaurant.set_city(city)
            phone = form.data['phone']
            restaurant.set_phone(phone)
            menu_type = form.data['menu_type']
            restaurant.set_menu_type(menu_type)

            RestaurantManager.update_restaurant(restaurant)
            return redirect(url_for('auth.operator', id=id_op))

    return render_template('update_restaurant.html', form=form)


@restaurants.route('/show_people/<int:id_op>/<int:rest_id>', methods=['GET', 'POST'])
@login_required
def show_people(id_op, rest_id):
    form = FilterForm()
    return redirect(url_for('auth.operator', id=id_op))