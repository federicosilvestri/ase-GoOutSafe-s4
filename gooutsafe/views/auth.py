from flask import Blueprint, render_template, redirect
from flask_login import (logout_user, login_user, login_required)
from werkzeug.security import generate_password_hash, check_password_hash

from gooutsafe import db
from gooutsafe.forms import LoginForm
from gooutsafe.models.user import User
from gooutsafe.models.restaurant import Restaurant
from gooutsafe.dao.user_manager import UserManager

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
                return redirect('/operator/'+ str(user.id))
            elif user.type == 'customer':
                return render_template('customer_profile.html', current_user=user)
            else: 
                return render_template('authority_profile.html', current_user=user)

    return render_template('login.html', form=form)


@auth.route('/profile/<int:id>', methods=['GET', 'POST'])
@login_required
def profile(id):
    return render_template('customer_profile.html')


@auth.route('/operator/<int:id>', methods=['GET', 'POST'])
@login_required
def operator(id):
    restaurant = Restaurant.query.filter_by(owner_id=id).first()
    return render_template('operator_profile.html', restaurant=restaurant)


@auth.route('/authority', methods=['GET', 'POST'])
@login_required
def authority():
    return render_template('authority_profile.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')
