from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required

from gooutsafe import db
from gooutsafe.auth import current_user
from gooutsafe.models.restaurant import Restaurant
from gooutsafe.dao.restaurant_manager import RestaurantManager
from gooutsafe.forms.home import HomeForm


home = Blueprint('home', __name__)


@home.route('/', methods=['GET', 'POST'])
def index():
    form = HomeForm()
    restaurants=[]
    if request.method == 'POST':
        if form.is_submitted():
            search_field = form.data['search_field']
            search_filter = form.data['filters']
            restaurants = search_by(search_field, search_filter)
        return render_template("index.html", restaurants = restaurants, form = form)
    
    return render_template("index.html", form = form)

def search_by(search_field, search_filter):
    if search_filter == "Name":
        restaurants = RestaurantManager.retrieve_by_restaurant_name(search_field)
        return restaurants
    if search_filter == "City":
        restaurants = RestaurantManager.retrieve_by_restaurant_city(search_field)
        return restaurants


    
