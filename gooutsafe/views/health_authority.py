from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from gooutsafe.auth import current_user
from gooutsafe.dao.customer_manager import CustomerManager
from gooutsafe.dao.reservation_manager import ReservationManager
from gooutsafe.dao.restaurant_manager import RestaurantManager
from gooutsafe.forms.authority import AuthorityForm
from gooutsafe.models.customer import Customer
from gooutsafe.models.reservation import Reservation
from gooutsafe.tasks.health_authority_tasks import (
    notify_restaurant_owners_about_positive_booked_customer,
    notify_restaurant_owners_about_positive_past_customer,
    schedule_revert_customer_health_status)

authority = Blueprint('authority', __name__)


@authority.route('/ha/search_customer', methods = ['GET','POST'])
@login_required
def search_customer():
    form = AuthorityForm()
    customer = None
    if request.method == 'POST':
        track_type = form.data['track_type']
        customer_ident = form.data['customer_ident']
        if(track_type == 'SSN'):
            customer = CustomerManager.retrieve_by_ssn(ssn=customer_ident)
        elif(track_type == 'Email'):
            customer = CustomerManager.retrieve_by_email(email=customer_ident)
            print(customer.email)
        else:
            customer = CustomerManager.retrieve_by_phone(phone=customer_ident)
        if customer is None:
            flash("The customer doesn't exist")
            return redirect(url_for('auth.authority', id=current_user.id, positive_id=0))
    return redirect(url_for('auth.authority', id=current_user.id, positive_id=customer.id))

@authority.route('/ha/mark_positive/<customer_id>', methods = ['GET','POST'])
@login_required
def mark_positive(customer_id):
    form = AuthorityForm()
    if request.method == 'POST':
        customer = CustomerManager.retrieve_by_id(id_=customer_id)
        if(customer.health_status):
            flash("Customer is already set to positive!")
        else:
            customer.set_health_status(status=True)
            CustomerManager.update_customer(customer)
            schedule_revert_customer_health_status(customer)
            notify_restaurant_owners_about_positive_past_customer(customer)
            notify_restaurant_owners_about_positive_booked_customer(customer)
            flash("Customer set to positive!")
    pos_customers = CustomerManager.retrieve_all_positive()    
    return render_template('authority_profile.html', form=form, pos_customers=pos_customers, search_customer=None)

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
            cust = CustomerManager.retrieve_by_id(c.user_id)
            cust_contacs.append(cust)
            restaurant_contacs.append(RestaurantManager.retrieve_by_id(c.restaurant_id).name)
            date_contacts.append(c.start_time.date())
    return render_template('contact_tracing_positive.html', customer=customer, pos_contact=cust_contacs, res_contact=restaurant_contacs, date_contact=date_contacts)
