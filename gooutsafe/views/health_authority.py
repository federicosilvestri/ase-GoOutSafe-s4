from flask import Blueprint, render_template
from flask_login import (logout_user, login_user, login_required)

from gooutsafe.auth import current_user
from gooutsafe.forms.authority import AuthorityForm

authority = Blueprint('authority', __name__)


@authority.route('/mark_positive', methods = ['POST'])
@login_required
def mark_positive():
    #TODO: implement this method
    form = AuthorityForm()
    return render_template('authority_profile.html', form=form)