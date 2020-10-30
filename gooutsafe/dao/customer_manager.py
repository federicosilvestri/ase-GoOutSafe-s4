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
    def update_customer(customer: Customer):
        Manager.update(customer=customer)

    @staticmethod
    def delete_customer(customer: Customer):
        Manager.delete(customer=customer)

    @staticmethod
    def delete_customer_by_id(id_):
        customer = CustomerManager.retrieve_by_id(id_)
        CustomerManager.delete_customer(customer)
