from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import (logout_user, login_user, login_required)
from werkzeug.security import generate_password_hash
from gooutsafe.dao.user_manager import UserManager
from gooutsafe.forms import UserForm, LoginForm
from gooutsafe.models.customer import Customer
from gooutsafe.models.operator import Operator

users = Blueprint('users', __name__)


@users.route('/users')
def _users():
    usrs = UserManager.retrieve()
    return render_template("users.html", users=usrs)


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
    UserManager.delete_user_by_id(id_)
<<<<<<< HEAD
    return redirect(url_for('home.index'))
=======
    return redirect('/')
>>>>>>> c4fda6543f8c472a44020d319012a81a2a964ce8
