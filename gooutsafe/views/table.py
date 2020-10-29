from flask import Blueprint, render_template

from gooutsafe.auth import current_user
from gooutsafe.models.restaurant import Restaurant
from gooutsafe.models.table import Table

table = Blueprint('table', __name__)


@table.route('/table/create_table')
def create_table():
    #TODO: implement this method
    pass

@table.route('/delete_table/<int:id>')
def delete_table():
    #TODO: implement this method
    pass

@table.route('/table/<table_id>')
def table_details(table_id):
    table = db.session.query(Table).flter_by(id=int(table_id)).all()[0]
    reservations = table.reservations
    restaurant = table.restaurant
    return render_template("table_details.html", table = table, reservations = reservations, restaurant = restaurant)