from flask import Blueprint, render_template, request
from flask_login import login_required, login_user, logout_user
from gooutsafe.auth import current_user
from gooutsafe.dao.customer_manager import CustomerManager
from gooutsafe.dao.reservation_manager import ReservationManager
from gooutsafe.dao.restaurant_manager import RestaurantManager
from gooutsafe.models.customer import Customer
from gooutsafe.models.reservation import Reservation
from gooutsafe.forms.authority import AuthorityForm

from gooutsafe.forms.authority import AuthorityForm

from gooutsafe.tasks.health_authority_tasks import schedule_revert_customer_health_status


from gooutsafe.forms.authority import AuthorityForm

from gooutsafe.tasks.health_authority_tasks import schedule_revert_customer_health_status


authority = Blueprint('authority', __name__)


@authority.route('/ha/mark_positive', methods = ['GET','POST'])
@login_required
def mark_positive():
    form = AuthorityForm()
    if request.method == 'POST':
        track_type = form.data['track_type']
        customer_ident = form.data['customer_ident']
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
    pos_customers = CustomerManager.retrieve_all_positive()    
    return render_template('authority_profile.html', form=form, pos_customers=pos_customers)

@authority.route('/ha/contact/<int:contact_id>', methods = ['GET'])
@login_required
def contact_tracing(contact_id):
    customer = CustomerManager.retrieve_by_id(id_=contact_id)
    #retrieve all the reservations for the positive customer
    pos_reservations = ReservationManager.retrieve_by_customer_id(user_id=customer.id)
    cust_contacs = []
    restaurant_contacs = []
    date_contacts = []
    for res in pos_reservations:
        #all reservations that intersect with the positive one
        contacs = ReservationManager.retrieve_all_contact_reservation_by_id(res.id)
        for c in contacs:
            #discard the reservations for the same positive customer
            if (customer.id != c.user_id):
                cust = CustomerManager.retrieve_by_id(c.user_id)
                cust_contacs.append(cust)
                restaurant_contacs.append(RestaurantManager.retrieve_by_id(c.restaurant_id).name)
                date_contacts.append(c.start_time.date())
    return render_template('contact_tracing_positive.html', customer=customer, pos_contact=cust_contacs, res_contact=restaurant_contacs, date_contact=date_contacts)
