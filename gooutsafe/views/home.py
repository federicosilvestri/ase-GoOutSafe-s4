import json

from flask import Blueprint, render_template, request, flash
from flask_login import current_user

from gooutsafe.dao.restaurant_manager import RestaurantManager
from gooutsafe.forms.restaurant_search import RestaurantSearchForm

home = Blueprint('home', __name__)


@home.route('/', methods=['GET', 'POST'])
def index():
    form = RestaurantSearchForm()
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


@home.route('/search', methods=['GET'])
def search():
    # this variable will not be used to retrieve data, because we use GET type and not POST
    form = RestaurantSearchForm()

    keyword = request.args.get('keyword', default=None, type=str)
    filters = request.args.get('filters', default=None, type=str)

    keyword = None if keyword is None or len(keyword) == 0 else keyword

    json_list = []
    if keyword is not None and filters is None:
        # searching by name
        restaurants = search_by(keyword, form.DEFAULT_SEARCH_FILTER)
    elif keyword is not None and filters is not None:
        restaurants = search_by(keyword, filters)
    else:
        restaurants = RestaurantManager.retrieve_all()
        #create a json object to show markers on a map
        for r in restaurants:
            json_list.append({"name": r.name, "lat": r.lat, "lon": r.lon })
        json_list = json.dumps(json_list)

    return render_template('explore.html', search_form=form, restaurants=restaurants, json_res=json_list)


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
