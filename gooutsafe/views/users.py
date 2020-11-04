from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import (logout_user, login_user, login_required)
from werkzeug.security import generate_password_hash

from gooutsafe.dao.user_manager import UserManager
from gooutsafe.dao.restaurant_manager import RestaurantManager

from gooutsafe.forms import UserForm, LoginForm
from gooutsafe.forms.update_customer import UpdateCustomerForm

from gooutsafe.models.customer import Customer
from gooutsafe.models.operator import Operator

from datetime import date

users = Blueprint('users', __name__)



@users.route('/create_user/<string:type>', methods=['GET', 'POST'])
def create_user_type(type):
    form = LoginForm()
    if type == "customer":
        form = UserForm()
        user = Customer()   
    else:
        user = Operator()

    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.data['email']
            searched_user = UserManager.retrieve_by_email(email)
            if searched_user is not None:
                flash ("Data already present in the database.")
                return render_template('create_user.html', form=form)
                
            form.populate_obj(user)
            user.set_password(generate_password_hash(form.password.data))

            UserManager.create_user(user)

            login_user(user)
            user.authenticated = True

            if user.type == 'operator':
                return redirect(url_for('auth.operator', id=user.id))
            else:
                return redirect(url_for('auth.profile', id=user.id))

    return render_template('create_user.html', form=form)


@users.route('/delete_user/<int:id_>', methods=['GET', 'POST'])
@login_required
def delete_user(id_):
    user = UserManager.retrieve_by_id(id_)
    if user.type == "operator":
        restaurant = RestaurantManager.retrieve_by_operator_id(id_)
        RestaurantManager.delete_restaurant(restaurant)

    UserManager.delete_user_by_id(id_)
    return redirect(url_for('home.index'))


@users.route('/update_user/<int:id>', methods=['GET', 'POST'])
@login_required
def update_user(id):
    user = UserManager.retrieve_by_id(id)
    if user.type == "customer":
        form = UpdateCustomerForm()
    elif user.type == "operator":
        form = LoginForm()

    if request.method == "POST":
        if form.is_submitted():
            email = form.data['email']
            searched_user = UserManager.retrieve_by_email(email)
            if searched_user is not None and id != searched_user.id:
                flash ("Data already present in the database.")
                return render_template('update_customer.html', form=form)

            password = form.data['password']
            user.set_email(email)            
            user.set_password(generate_password_hash(password))

            if user.type == "customer": 
                phone = form.data['phone']
                user.set_phone(phone)
                UserManager.update_user(user)

                return redirect(url_for('auth.profile', id=user.id))
            
            elif user.type == "operator":         
                UserManager.update_user(user)
                return redirect(url_for('auth.operator', id=user.id))

    return render_template('update_customer.html', form=form)