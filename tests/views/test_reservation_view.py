from flask import url_for
from faker import Faker
import datetime

from tests.models.test_reservation import TestReservation
from tests.models.test_restaurant import TestRestaurant
from tests.models.test_customer import TestCustomer
from tests.models.test_table import TestTable
from tests.models.test_restaurant_availability import TestRestaurantAvailability


from tests.views.view_test import ViewTest


class TestReservationView(ViewTest):
    faker = Faker('it_IT')

    @classmethod
    def setUpClass(cls):
        super(TestReservationView, cls).setUpClass()

        from gooutsafe.views import reservation
        from gooutsafe.views import home

        from gooutsafe.dao import reservation_manager, customer_manager, restaurant_manager
        from gooutsafe.dao import restaurant_availability_manager, table_manager
        
        cls.reservation_manager = reservation_manager.ReservationManager
        cls.customer_manager = customer_manager.CustomerManager
        cls.restaurant_manager = restaurant_manager.RestaurantManager
        cls.ava_manager = restaurant_availability_manager.RestaurantAvailabilityManager
        cls.table_manager = table_manager.TableManager





    def test_create_reservation(self):
        from gooutsafe.models import Restaurant, Table, RestaurantAvailability
        self.login_test_customer()
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        self.restaurant_manager.create_restaurant(restaurant)
        table = Table(4, restaurant)
        self.table_manager.create_table(table)
        start_ava = datetime.time(hour=8)
        end_ava = datetime.time(hour=16)
        ava = RestaurantAvailability(restaurant.id, 'Monday', start_time=start_ava, end_time=end_ava)
        rv = self.client.get('/create_reservation/' + str(restaurant.id))
        assert rv.status_code == 200    
        start_date = datetime.date(year=2020, month=11, day=9)
        start_time = datetime.time(hour=13, minute=30)
        
        data = dict(start_date=start_date, start_time=start_time,people_number=1)
        rv = self.client.post('/create_reservation/' + str(restaurant.id), 
                            data=data, 
                            follow_redirects=True
                            )
        assert rv.status_code == 200
        start_date = datetime.date(year=2020, month=11, day=9)
        start_time = datetime.time(hour=19, minute=30)
        data = dict(start_date=start_date, start_time=start_time,people_number=1)
        rv = self.client.post('/create_reservation/' + str(restaurant.id), 
                            data=data, 
                            follow_redirects=True
                            )
        assert rv.status_code == 200
        start_date = datetime.date(year=2020, month=11, day=9)
        start_time = datetime.time(hour=12, minute=30)
        
        data = dict(start_date=start_date, start_time=start_time,people_number=50)
        rv = self.client.post('/create_reservation/' + str(restaurant.id), 
                            data=data, 
                            follow_redirects=True
                            )
        assert rv.status_code == 200

        




    def test_customer_my_reservation(self):
        rv = self.client.get('/customer/my_reservations')
        assert rv.status_code == 200

    def test_confirm_reservation(self):
        self.login_test_customer()
        reservation,_ = TestReservation.generate_random_reservation()
        self.reservation_manager.create_reservation(reservation)
        rv = self.client.get('/reservation/confirm/' + str(reservation.id), follow_redirects=True)
        assert rv.status_code == 200
    
    def test_edit_reservation(self):
        customer = self.login_test_customer()
        reservation,_ = TestReservation.generate_random_reservation(user=customer)
        self.reservation_manager.create_reservation(reservation)
        rv = self.client.get('/edit/' + str(reservation.id) +'/'+ str(customer.id))
        assert rv.status_code == 200
