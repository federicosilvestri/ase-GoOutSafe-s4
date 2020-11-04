from flask import Blueprint, render_template, request, flash

from flask_login import current_user
from gooutsafe.dao.restaurant_manager import RestaurantManager
from gooutsafe.forms.restaurant_search import HomeForm

home = Blueprint('home', __name__)


@home.route('/', methods=['GET', 'POST'])
def index():
    form = HomeForm()
    if request.method == 'POST':
        if form.is_submitted():
            search_field = form.data['search_field']
            search_filter = form.data['filters']
            if not search_field:
                restaurants = RestaurantManager.retrieve_all()
                print("MOSTRA TUTTI I RISTORANTI")
            else:
                restaurants = search_by(search_field, search_filter).all()
                if not restaurants:
                    flash("There aren't restaurants for this search")
            return render_template("index.html", restaurants=restaurants, form=form, current_user=current_user)
    return render_template("index.html", form=form, current_user=current_user)


def search_by(search_field, search_filter):
    if search_filter == "Name":
        restaurants = RestaurantManager.retrieve_by_restaurant_name(search_field)
        return restaurants
    if search_filter == "City":
        restaurants = RestaurantManager.retrieve_by_restaurant_city(search_field)
        return restaurants
    if search_filter == "Menu Type":
        restaurants = RestaurantManager.retrieve_by_menu_type(search_field)
        return restaurants
