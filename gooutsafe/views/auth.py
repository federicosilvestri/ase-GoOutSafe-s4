from flask import Blueprint, render_template, redirect, url_for
from flask_login import (logout_user, login_user, login_required)
from werkzeug.security import generate_password_hash, check_password_hash

from gooutsafe import db
from gooutsafe.forms import LoginForm
from gooutsafe.forms.authority import AuthorityForm
from gooutsafe.forms.reservation import ReservationForm

from gooutsafe.models.user import User
from gooutsafe.models.restaurant import Restaurant

from gooutsafe.dao.user_manager import UserManager
from gooutsafe.dao.reservation_manager import ReservationManager
from gooutsafe.dao.customer_manager import CustomerManager
from gooutsafe.dao.restaurant_manager import RestaurantManager

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email, password = form.data['email'], form.data['password']
        q = UserManager.retrieve_by_id(email)
        q = db.session.query(User).filter(User.email == email)
        user = q.first()

        if user is not None and check_password_hash(user.password, password):
            login_user(user)
            if user.type == 'operator':
                return redirect(url_for('auth.operator', id=user.id))
            elif user.type == 'customer':
                return redirect(url_for('auth.profile', id=user.id))
            else:
                ha_form = AuthorityForm()
                pos_customers = CustomerManager.retrieve_all_positive()
                return render_template('authority_profile.html', current_user=user, form = ha_form, pos_customers=pos_customers)

    return render_template('login.html', form=form)


@auth.route('/profile/<int:id>', methods=['GET', 'POST'])
@login_required
def profile(id):
    reservations = ReservationManager.retrieve_by_customer_id(id)
    form = ReservationForm()
    customer = CustomerManager.retrieve_by_id(id)
    restaurants = RestaurantManager.retrieve_all()
    return render_template('customer_profile.html', customer=customer, 
            reservations=reservations, restaurants=restaurants, form=form)


@auth.route('/operator/<int:id>', methods=['GET', 'POST'])
@login_required
def operator(id):
    restaurant = RestaurantManager.retrieve_by_operator_id(id)
    return render_template('operator_profile.html', restaurant=restaurant)


@auth.route('/authority', methods=['GET', 'POST'])
@login_required
def authority():
    return render_template('authority_profile.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.index'))
