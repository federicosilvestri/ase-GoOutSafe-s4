from faker import Faker
from datetime import timedelta, datetime
from models.test_reservation import TestReservation
from models.test_customer import TestCustomer
from models.test_restaurant import TestRestaurant
from models.test_user import TestUser
from models.test_table import TestTable



from .dao_test import DaoTest


class TestReservationManager(DaoTest):
    faker = Faker('it_IT')

    def setUp(self):
        super(TestReservationManager, self).setUp()

        from gooutsafe.dao import reservation_manager
        self.reservation_manager = reservation_manager.ReservationManager
        from gooutsafe.dao import customer_manager
        self.customer_manager = customer_manager.CustomerManager
        from gooutsafe.dao import user_manager
        self.user_manager = user_manager.UserManager
        from gooutsafe.dao import restaurant_manager
        self.restaurant_manager = restaurant_manager.RestaurantManager        
        from gooutsafe.dao import table_manager
        self.table_manager = table_manager.TableManager
        from gooutsafe.dao import customer_manager
        self.customer_manager = customer_manager.CustomerManager

    
    
    def test_create_reservation(self):
        reservation1, _ = TestReservation.generate_random_reservation()
        self.reservation_manager.create_reservation(reservation=reservation1)
        reservation2 = self.reservation_manager.retrieve_by_id(id_=reservation1.id)
        TestReservation.assertEqualReservations(reservation1, reservation2)

    def test_delete_reservation(self):
        base_reservation, _ = TestReservation.generate_random_reservation()
        self.reservation_manager.create_reservation(reservation=base_reservation)
        self.reservation_manager.delete_reservation(base_reservation)
        self.assertIsNone(self.reservation_manager.retrieve_by_id(base_reservation.id))

    def test_delete_reservation_by_id(self):
        base_reservation, _ = TestReservation.generate_random_reservation()
        self.reservation_manager.create_reservation(reservation=base_reservation)
        self.reservation_manager.delete_reservation_by_id(base_reservation.id)
        self.assertIsNone(self.reservation_manager.retrieve_by_id(base_reservation.id))

    def test_update_reservation(self):
        base_reservation, _ = TestReservation.generate_random_reservation()
        self.reservation_manager.create_reservation(reservation=base_reservation)
        base_reservation.set_people_number(TestReservationManager.faker.random_int(min=0,max=15))
        start_time = TestReservationManager.faker.date_time_between('now','+6w')
        base_reservation.set_start_time(start_time)
        updated_reservation = self.reservation_manager.retrieve_by_id(id_=base_reservation.id)
        TestReservation.assertEqualReservations(base_reservation, updated_reservation)

    def test_retrieve_by_user_id(self):
        reservation, _ = TestReservation.generate_random_reservation()
        user = reservation.user
        self.user_manager.create_user(user=user)
        self.reservation_manager.create_reservation(reservation=reservation)
        retrieved_reservation = self.reservation_manager.retrieve_by_customer_id(user_id=user.id)
        for res in retrieved_reservation:
            TestReservation.assertEqualReservations(reservation, res)

    def test_retrieve_by_restaurant_id(self):
        reservation, _ = TestReservation.generate_random_reservation()
        restaurant = reservation.restaurant
        self.restaurant_manager.create_restaurant(restaurant=restaurant)
        self.reservation_manager.create_reservation(reservation=reservation)
        retrieved_reservation = self.reservation_manager.retrieve_by_restaurant_id(restaurant_id=restaurant.id)
        for res in retrieved_reservation:
            TestReservation.assertEqualReservations(reservation, res)
    
    def test_retrieve_by_table_id(self):
        reservation, _ = TestReservation.generate_random_reservation()
        table = reservation.table
        self.table_manager.create_table(table=table)
        self.reservation_manager.create_reservation(reservation=reservation)
        retrieved_reservation = self.reservation_manager.retrieve_by_table_id(table_id=table.id)
        for res in retrieved_reservation:
            TestReservation.assertEqualReservations(reservation, res)
    
    def test_retrieve_by_customer_id(self):
        reservation, _ = TestReservation.generate_random_reservation()
        customer = reservation.user
        self.customer_manager.create_customer(customer=customer)
        self.reservation_manager.create_reservation(reservation=reservation)
        retrieved_reservation = self.reservation_manager.retrieve_by_customer_id(user_id=customer.id)
        for res in retrieved_reservation:
            TestReservation.assertEqualReservations(reservation, res)

    def test_retrieve_all_contact_reservation_by_id(self):
        from gooutsafe.models.table import Table
        from gooutsafe.models.reservation import Reservation
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        self.restaurant_manager.create_restaurant(restaurant=restaurant)
        start_time_positive = datetime(year=2020, month=11, day=2, hour=11)
        end_time_positive = start_time_positive + timedelta(Reservation.MAX_TIME_RESERVATION)
        contacted_users = []
        for _ in range(0, self.faker.random_int(min=2, max=10)):
            table,_ = TestTable.generate_random_table(fixed_restaurant=restaurant)
            self.table_manager.create_table(table)
            start_time = self.faker.date_time_between_dates(datetime_start=start_time_positive, datetime_end=end_time_positive)
            contacted_user = TestUser.create_random_user()
            contacted_users.append(contacted_user)
            self.user_manager.create_user(contacted_user)
            reservation = Reservation(contacted_user, table, restaurant, 1, start_time)
            self.reservation_manager.create_reservation(reservation)

        table1, _= TestTable.generate_random_table(fixed_restaurant=restaurant)
        positive_user = TestUser.create_random_user()
        self.user_manager.create_user(positive_user)
        positive_reservation = Reservation(positive_user, table1, restaurant, 1, start_time_positive)
        self.reservation_manager.create_reservation(positive_reservation)
        retriverd_contacted_reservations = self.reservation_manager.retrieve_all_contact_reservation_by_id(positive_reservation.id)
        retriverd_contacted_users = []
        for res in retriverd_contacted_reservations:
            retriverd_contacted_users.append(res.user)
        retriverd_contacted_users.sort(key=lambda positive_user: positive_user.id)
        contacted_users.sort(key=lambda positive_user: positive_user.id)
        for retriverd_contacted_user, contacted_user in zip(retriverd_contacted_users, contacted_users):
            TestUser.assertUserEquals(contacted_user, retriverd_contacted_user)


 