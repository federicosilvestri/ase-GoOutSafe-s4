from flask import Blueprint, render_template, redirect
from flask_login import (logout_user, login_user, login_required)

from gooutsafe import db
from gooutsafe.forms import LoginForm
from gooutsafe.models.user import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email, password = form.data['email'], form.data['password']
        q = db.session.query(User).filter(User.email == email)
        user = q.first()

        if user is not None and user.authenticate(password):
            login_user(user)

            if (user.type == 'operator'):
                return redirect('/operator')
            else:
                return redirect('/profile')

    return render_template('login.html', form=form)


# TODO: put the current_user
@auth.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('customer_profile.html')


# TODO: put the current_user
@auth.route('/operator', methods=['GET', 'POST'])
def operator():
    return render_template('operator_profile.html')


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    user.authenticated = False
    return redirect('/')
