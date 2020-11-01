from flask import Blueprint, render_template, request
from flask_login import login_required, login_user, logout_user
from gooutsafe.auth import current_user
from gooutsafe.dao.customer_manager import CustomerManager
from gooutsafe.dao.reservation_manager import ReservationManager
from gooutsafe.models.customer import Customer
from gooutsafe.models.reservation import Reservation
from gooutsafe.forms.authority import AuthorityForm

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
            #schedule_revert_customer_health_status(customer)
    form = AuthorityForm()
    pos_customers = CustomerManager.retrieve_all_positive()
    return render_template('authority_profile.html', form=form, pos_customers=pos_customers)

@authority.route('/ha/contact/<int:contact_id>', methods = ['GET'])
@login_required
def contact_tracing(contact_id):
    customer = CustomerManager.retrieve_by_id(id_=contact_id)
    pos_reservations = ReservationManager.retrieve_by_customer_id(user_id=customer.id)
    all_contacs = []
    count = 1
    for res in pos_reservations:
        print("Reservation numero: ",count)
        count+=1
        print(res.start_time, res.end_time, res.restaurant_id, res.user_id)
        contacs = ReservationManager.retrieve_all_contact_reservation_by_id(res.id)
        print("Numero di contatti: (compreso lo stesso positivo):",len(contacs))
        for c in contacs:
            if (customer.id != c.user_id):
                print(c.start_time, c.end_time,c.restaurant_id, c.user_id)
                print("CONTATTO")
                cust = CustomerManager.retrieve_by_id(c.user_id)
                all_contacs.append(cust)
            else:
                print("PRENOTAZIONE DELLO STESSO UTENTE")
    return render_template('contact_tracing_positive.html', customer=customer, pos_contact=all_contacs,  )
