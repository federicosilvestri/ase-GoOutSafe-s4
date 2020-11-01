from flask import Blueprint, redirect, render_template, request
from flask_login import (logout_user, login_user, login_required)

from gooutsafe import db
from gooutsafe.models.like import Like
from gooutsafe.models.restaurant import Restaurant
from gooutsafe.models.table import Table
from gooutsafe.models.restaurant_availability import RestaurantAvailability
from gooutsafe.forms.restaurant import RestaurantForm
from gooutsafe.forms.add_table import TableForm
from gooutsafe.forms.add_times import TimesForm
from gooutsafe.forms.add_measure import MeasureForm
from gooutsafe.dao.restaurant_manager import RestaurantManager
from gooutsafe.dao.table_manager import TableManager
from gooutsafe.dao.restaurant_availability_manager import RestaurantAvailabilityManager


restaurants = Blueprint('restaurants', __name__)


@restaurants.route('/restaurants')
def _restaurants(message=''):
    allrestaurants = db.session.query(Restaurant)
    return render_template("restaurants.html", message=message, restaurants=allrestaurants,
                           base_url="http://127.0.0.1:5000/restaurants")


@restaurants.route('/restaurants/<restaurant_id>')
@login_required
def restaurant_sheet(restaurant_id):
    restaurant = RestaurantManager.retrieve_by_id(id_=restaurant_id)
    return render_template("restaurantsheet.html", restaurant=restaurant)


@restaurants.route('/restaurants/like/<restaurant_id>')
@login_required
def _like(restaurant_id):
    q = Like.query.filter_by(liker_id=current_user.id, restaurant_id=restaurant_id)

    if q.first() is not None:
        new_like = Like()
        new_like.liker_id = current_user.id
        new_like.restaurant_id = restaurant_id
        db.session.add(new_like)
        db.session.commit()
        message = ''
    else:
        message = 'You\'ve already liked this place!'
    return _restaurants(message)


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
            restaurant = Restaurant(name,address, city, 0, 0, phone, menu_type)
            restaurant.owner_id = id_op

            RestaurantManager.create_restaurant(restaurant)

            return redirect('/operator/'+ str(id_op))

    return render_template('create_restaurant.html', form=form)


@restaurants.route('/restaurants/details/<int:id_op>', methods=['GET', 'POST'])
@login_required
def details(id_op):
    table_form = TableForm()
    time_form = TimesForm()
    measure_form = MeasureForm()
    restaurant = RestaurantManager.retrieve_by_operator_id(id_op)
    tables = TableManager.retrieve_by_restaurant_id(restaurant.id)
    ava = restaurant.availabilities

    return render_template('add_restaurant_details.html', 
                    restaurant=restaurant, tables=tables, 
                    table_form=table_form, time_form=time_form,
                    times=ava, measure_form=measure_form)


@restaurants.route('/restaurants/save/<int:id_op>/<int:rest_id>', methods=['GET', 'POST'])
@login_required
def save_details(id_op, rest_id):
    table_form = TableForm()
    time_form = TimesForm()
    measure_form = MeasureForm()
    restaurant = RestaurantManager.retrieve_by_operator_id(id_op)
    tables = TableManager.retrieve_by_restaurant_id(restaurant.id)
    ava = restaurant.availabilities

    if request.method == "POST":
        if table_form.is_submitted():
            num_tables = table_form.data['number']
            capacity = table_form.data['max_capacity']

            for i in range(0,num_tables):
                if max_capacity >= 1:
                    table = Table(capacity=capacity, restaurant=restaurant)
                    TableManager.create_table(table)
            
            return redirect('/restaurants/save/'+ str(id_op) + '/' +str(rest_id))

    return render_template('add_restaurant_details.html', 
                    restaurant=restaurant, tables=tables, 
                    table_form=table_form, time_form=time_form, 
                    times=ava, measure_form=measure_form)


@restaurants.route('/restaurants/savetime/<int:id_op>/<int:rest_id>', methods=['GET', 'POST'])
@login_required
def save_time(id_op, rest_id):
    table_form = TableForm()
    time_form = TimesForm()
    measure_form = MeasureForm()
    restaurant = RestaurantManager.retrieve_by_operator_id(id_op)
    tables = TableManager.retrieve_by_restaurant_id(restaurant.id)
    ava = restaurant.availabilities

    if request.method == "POST":
        if time_form.is_submitted():
            start_time = time_form.data['start_time']
            end_time = time_form.data['end_time']

            if end_time > start_time:
                time = RestaurantAvailability(rest_id, start_time, end_time)
                RestaurantAvailabilityManager.create_availability(time)
            
            return redirect('/restaurants/save/'+ str(id_op) + '/' +str(rest_id))

    return render_template('add_restaurant_details.html', 
                    restaurant=restaurant, tables=tables, 
                    table_form=table_form, time_form=time_form, 
                    times=ava, measure_form=measure_form)