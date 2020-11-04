from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import (logout_user, login_user, login_required)
from werkzeug.security import check_password_hash

from gooutsafe.auth import current_user

from gooutsafe.dao.customer_manager import CustomerManager
from gooutsafe.dao.user_manager import UserManager
from gooutsafe.forms import LoginForm
from gooutsafe.forms.authority import AuthorityForm
from gooutsafe.forms.reservation import ReservationForm
from gooutsafe.forms.filter_form import FilterForm

from gooutsafe.models.restaurant import Restaurant

from gooutsafe.dao.user_manager import UserManager
from gooutsafe.dao.reservation_manager import ReservationManager
from gooutsafe.dao.customer_manager import CustomerManager
from gooutsafe.dao.restaurant_manager import RestaurantManager
from gooutsafe.dao.health_authority_manager import AuthorityManager
from gooutsafe.dao.notification_manager import NotificationManager

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.is_submitted():
        email, password = form.data['email'], form.data['password']
        user = UserManager.retrieve_by_email(email)

        if user is not None and check_password_hash(user.password, password):
            login_user(user)
            if user.type == 'operator':
                return redirect('/operator/%d' % user.id)
            elif user.type == 'customer':
                return redirect('/profile/%d' % user.id)
            else:
                return redirect('/authority/%d/0' % user.id)
        else:
            flash('Invalid credentials')

    return render_template('login.html', form=form)


@auth.route('/profile/<int:id>', methods=['GET', 'POST'])
@login_required
def profile(id):
    if current_user.id == id:
        reservations = ReservationManager.retrieve_by_customer_id(id)
        form = ReservationForm()
        filter_form = FilterForm()
        customer = CustomerManager.retrieve_by_id(id)
        restaurants = RestaurantManager.retrieve_all()
        return render_template('customer_profile.html', customer=customer, 
                reservations=reservations, restaurants=restaurants, form=form, filter_form=filter_form)
    return redirect(url_for('home.index'))


@auth.route('/operator/<int:id>', methods=['GET', 'POST'])
@login_required
def operator(id):
    if current_user.id == id:
        restaurant = Restaurant.query.filter_by(owner_id=id).first()
        return render_template('operator_profile.html', restaurant=restaurant)
    return redirect(url_for('home.index'))


@auth.route('/authority/<int:id>/<int:positive_id>', methods=['GET', 'POST'])
@login_required
def authority(id, positive_id):
    if current_user.id == id:
        authority = AuthorityManager.retrieve_by_id(id)
        ha_form = AuthorityForm()
        pos_customers = CustomerManager.retrieve_all_positive()
        search_customer = CustomerManager.retrieve_by_id(positive_id)
        return render_template('authority_profile.html', current_user=authority, 
            form=ha_form, pos_customers=pos_customers, search_customer=search_customer)
    return redirect(url_for('home.index'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@auth.route('/notifications', methods=['GET'])
@login_required
def notifications():
    notifications = NotificationManager.retrieve_by_target_user_id(current_user.id)
    # sort them by date
    # divide them in new and old for the operator
    processed_notification_info = []
    if current_user.type == "customer":
        for notification in notifications:
            restaurant_name = RestaurantManager.retrieve_by_id(notification.contagion_restaurant_id).name
            processed_notification_info.append({"timestamp": notification.timestamp,
                                                 "contagion_datetime": notification.contagion_datetime,
                                                 "contagion_restaurant_name": restaurant_name})
        return render_template('customer_notifications.html', current_user=current_user, notifications=processed_notification_info)
    elif current_user.type == "operator":
        for notification in notifications:
            info = {"timestamp": notification.timestamp,
                    "contagion_datetime": notification.contagion_datetime}
            is_future = notification.timestamp < notification.contagion_datetime
            info['is_future'] = is_future
            if is_future:
                customer_phone_number = UserManager.retrieve_by_id(notification.positive_customer_id).phone
                info['customer_phone_number'] = customer_phone_number
            processed_notification_info.append(info)
        return render_template('operator_notifications.html', current_user=current_user, notifications=processed_notification_info)
    