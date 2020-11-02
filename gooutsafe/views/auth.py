from flask import Blueprint, render_template, redirect
from flask_login import (logout_user, login_user, login_required)
from werkzeug.security import check_password_hash

from gooutsafe.dao.customer_manager import CustomerManager
from gooutsafe.dao.user_manager import UserManager
from gooutsafe.forms import LoginForm
from gooutsafe.forms.authority import AuthorityForm
from gooutsafe.models.restaurant import Restaurant

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    login_error = False

    if form.is_submitted():
        email, password = form.data['email'], form.data['password']
        user = UserManager.retrieve_by_email(email)

        if user is not None and check_password_hash(user.password, password):
            login_user(user)
            if user.type == 'operator':
                return redirect('/operator/%d' % user.id)
            elif user.type == 'customer':
                return render_template('customer_profile.html', current_user=user)
            else:
                ha_form = AuthorityForm()
                pos_customers = CustomerManager.retrieve_all_positive()
                return render_template('authority_profile.html', current_user=user, form=ha_form,
                                       pos_customers=pos_customers)
        else:
            login_error = True

    return render_template('login.html', form=form, login_error=login_error)


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
