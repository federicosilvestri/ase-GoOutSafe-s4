from faker import Faker
from models.test_restaurant import TestRestaurant
from models.test_operator import TestOperator


from .dao_test import DaoTest


class TestRestaurantManager(DaoTest):
    faker = Faker('it_IT')

    def setUp(self):
        super(TestRestaurantManager, self).setUp()

        from gooutsafe.dao import restaurant_manager
        self.restaurant_manager = restaurant_manager.RestaurantManager
        from gooutsafe.dao import customer_manager
        self.customer_manager = customer_manager.CustomerManager
    
    def test_create_restaurant(self):
        restaurant1, _ = TestRestaurant.generate_random_restaurant()
        self.restaurant_manager.create_restaurant(restaurant=restaurant1)
        restaurant2 = self.restaurant_manager.retrieve_by_id(id_=restaurant1.id)
        TestRestaurant.assertEqualRestaurants(restaurant1, restaurant2)
    
    def test_delete_restaurant(self):
        base_restaurant, _ = TestRestaurant.generate_random_restaurant()
        self.restaurant_manager.create_restaurant(restaurant=base_restaurant)
        self.restaurant_manager.delete_restaurant(base_restaurant)
        self.assertIsNone(self.restaurant_manager.retrieve_by_id(base_restaurant.id))

    def test_delete_restaurant_by_id(self):
        base_restaurant, _ = TestRestaurant.generate_random_restaurant()
        self.restaurant_manager.create_restaurant(restaurant=base_restaurant)
        self.restaurant_manager.delete_restaurant_by_id(base_restaurant.id)
        self.assertIsNone(self.restaurant_manager.retrieve_by_id(base_restaurant.id))

    def test_update_restaurant(self):
        base_restaurant, _ = TestRestaurant.generate_random_restaurant()
        self.restaurant_manager.create_restaurant(restaurant=base_restaurant)
        base_restaurant.set_address(TestRestaurantManager.faker.street_address())
        base_restaurant.set_city(TestRestaurantManager.faker.city())
        updated_restaurant = self.restaurant_manager.retrieve_by_id(id_=base_restaurant.id)
        TestRestaurant.assertEqualRestaurants(base_restaurant, updated_restaurant)

    def test_retrieve_by_operator_id(self):
        restaurant, _ = TestRestaurant.generate_random_restaurant()
        operator, _ = TestOperator.generator_random_operator()
        restaurant.owner = operator
        self.restaurant_manager.create_restaurant(restaurant=restaurant)
        self.customer_manager.create_customer(customer=operator)
        retrieved_restaurant = self.restaurant_manager.retrieve_by_operator_id(operator_id=operator.id)
        TestRestaurant.assertEqualRestaurants(restaurant, retrieved_restaurant)
