from flask import Blueprint, render_template, request
from flask_login import login_required, login_user, logout_user
from gooutsafe.auth import current_user
from gooutsafe.dao.customer_manager import CustomerManager
from gooutsafe.forms.authority import AuthorityForm
from gooutsafe.models.customer import Customer
from gooutsafe.tasks.health_authority_tasks import \
    schedule_revert_customer_health_status

authority = Blueprint('authority', __name__)


@authority.route('/ha/mark_positive', methods = ['POST'])
@login_required
def mark_positive():
    if request.method == 'POST':
        track_type = request.form['track_type']
        customer_ident = request.form['customer_ident']
        customer = None
        if(track_type == 'SSN'):
            customer = CustomerManager.retrieve_by_ssn(ssn=customer_ident)
        elif(track_type == 'email'):
            customer = CustomerManager.retrieve_by_email(email=customer_ident)
        else:
            customer = CustomerManager.retrieve_by_phone(phone=customer_ident)
        if(customer is not None):
            customer.set_health_status(status=True)
            CustomerManager.update_customer(customer)
            schedule_revert_customer_health_status(customer)
    form = AuthorityForm()
    pos_customers = CustomerManager.retrieve_all_positive()
    return render_template('authority_profile.html', form=form, pos_customers=pos_customers)

@authority.route('/ha/contact/<int:contact_id>', methods = ['GET'])
@login_required
def contact_tracing(contact_id):
    # TODO //visualize all contact with positive person
    customer = CustomerManager.retrieve_by_id(id_=contact_id)
    return render_template('contact_tracing_positive.html', customer=customer)
