from flask import Blueprint, redirect, render_template, request

from gooutsafe import db
from gooutsafe.forms import UserForm, OperatorForm, HealthAuthForm
from gooutsafe.models.user import User

users = Blueprint('users', __name__)


@users.route('/users')
def _users():
    users = db.session.query(User)
    return render_template("users.html", users=users)


@users.route('/create_user/<string:type>', methods=['GET', 'POST'])
def create_user_type(type):
    if (type == "<customer>"):
        form = UserForm()
    else:
        form = OperatorForm()

    """
    TODO: leave it for the tests
    else:
        form = HealthAuthForm()
    """

    #TODO: signup
    """  
    if request.method == 'POST':

        if form.validate_on_submit():
            new_user = User()
            form.populate_obj(new_user)
            new_user.set_password(form.password.data)  # pw should be hashed with some salt
            db.session.add(new_user)
            db.session.commit()
            return redirect('/users')
    """
    return render_template('create_user.html', form=form)
