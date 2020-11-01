from gooutsafe.models.customer import Customer
from .manager import Manager


class CustomerManager(Manager):

    @staticmethod
    def create_customer(customer: Customer):
        Manager.create(customer=customer)

    @staticmethod
    def retrieve_by_id(id_):
        Manager.check_none(id=id_)
        return Customer.query.get(id_)
    
    @staticmethod
    def retrieve_by_ssn(ssn):
        try:
            customer = Customer.query.filter_by(social_number=ssn).first()
            Manager.check_none(customer=customer)
            return CustomerManager.retrieve_by_id(id_=customer.id)
        except ValueError:
            return None

    @staticmethod
    def retrieve_by_email(email):
        try:
            customer = Customer.query.filter_by(email=email).first()
            Manager.check_none(customer=customer)
            return CustomerManager.retrieve_by_id(id_=customer.id)
        except ValueError:
            return None
    
    @staticmethod
    def retrieve_by_phone(phone):
        try:
            customer = Customer.query.filter_by(phone=phone).first()
            Manager.check_none(customer=customer)
            return CustomerManager.retrieve_by_id(id_=customer.id)
        except ValueError:
            return None 
            
    @staticmethod
    def retrieve_all_positive():
        pos_customers = Customer.query.filter_by(health_status=True).all()
        if (len(pos_customers) != 0):
            return pos_customers
        else:
            return None

    @staticmethod
    def update_customer(customer: Customer):
        Manager.update(customer=customer)

    @staticmethod
    def delete_customer(customer: Customer):
        Manager.delete(customer=customer)

    @staticmethod
    def delete_customer_by_id(id_):
        customer = CustomerManager.retrieve_by_id(id_)
        CustomerManager.delete_customer(customer)
