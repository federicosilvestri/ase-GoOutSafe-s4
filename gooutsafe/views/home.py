from flask import Blueprint, render_template

from gooutsafe import db
from gooutsafe.auth import current_user
from gooutsafe.models.restaurant import Restaurant
from gooutsafe.tasks.home_tasks import print_with_delay

home = Blueprint('home', __name__)


@home.route('/')
def index():
    if current_user is not None and hasattr(current_user, 'id'):
        restaurants = db.session.query(Restaurant)
    else:
        restaurants = None
    task = print_with_delay.delay()
    return render_template("index.html", restaurants=restaurants)
