from flask import Blueprint, redirect, render_template, request
from flask_login import (logout_user, login_user, login_required)

from gooutsafe import db
from gooutsafe.models.like import Like
from gooutsafe.models.restaurant import Restaurant
from gooutsafe.models.table import Table
from gooutsafe.forms.restaurant import RestaurantForm
from gooutsafe.dao.restaurant_manager import RestaurantManager
from gooutsafe.dao.table_manager import TableManager


restaurants = Blueprint('restaurants', __name__)


@restaurants.route('/restaurants')
def _restaurants(message=''):
    allrestaurants = db.session.query(Restaurant)
    return render_template("restaurants.html", message=message, restaurants=allrestaurants,
                           base_url="http://127.0.0.1:5000/restaurants")


@restaurants.route('/restaurants/<restaurant_id>')
@login_required
def restaurant_sheet(restaurant_id):
    record = db.session.query(Restaurant).filter_by(id=int(restaurant_id)).all()[0]
    return render_template("restaurantsheet.html", name=record.name, likes=record.likes, address=record.address,
                            city=record.city, lat=record.lat, lon=record.lon, menu_type=record.menu_type,
                            phone=record.phone)


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
    restaurant = RestaurantManager.retrieve_by_operator_id(id_op)
    #TODO table = 
    return render_template('add_restaurant_details.html', restaurant=restaurant)


@restaurants.route('/restaurants/save/<int:id_op>/<int:rest_id>', methods=['GET', 'POST'])
def save_details(id_op, rest_id):
    print("@@@@@@@@@@@@@@@@@@@")
    num_tables = request.form['num_tables']
    capacity = request.form['capacity']

    for i in range(0,num_tables):
        table = Table(capacity, rest_id)
        TableManager.create_table(table)

    return redirect ('/operator/'+str(id_op))
