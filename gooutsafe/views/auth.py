from flask import Blueprint, render_template, redirect
from flask_login import (logout_user, login_user, login_required)
from werkzeug.security import generate_password_hash, check_password_hash

from gooutsafe import db
from gooutsafe.forms import LoginForm
from gooutsafe.models.user import User
from gooutsafe.models.restaurant import Restaurant

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email, password = form.data['email'], form.data['password']
        q = db.session.query(User).filter(User.email == email)
        user = q.first()

        if user is not None and check_password_hash(user.password, password):
            login_user(user)
            if user.type == 'operator':
                return render_template('operator_profile.html', current_user=user)
            elif user.type == 'customer':
                return render_template('customer_profile.html', current_user=user)
            else: 
                return render_template('authority_profile.html', current_user=user)

    return render_template('login.html', form=form)


@auth.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('customer_profile.html')


@auth.route('/operator/<int:id>', methods=['GET', 'POST'])
@login_required
def operator(id):
    return render_template('operator_profile.html')


@auth.route('/authority', methods=['GET', 'POST'])
@login_required
def authority():
    return render_template('authority_profile.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')
