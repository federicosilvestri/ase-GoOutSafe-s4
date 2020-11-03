from gooutsafe.models.restaurant import Restaurant
from .manager import Manager


class RestaurantManager(Manager):

    @staticmethod
    def create_restaurant(restaurant: Restaurant):
        Manager.create(restaurant=restaurant)

    @staticmethod
    def retrieve_by_id(id_):
        Manager.check_none(id=id_)
        return Restaurant.query.get(id_)

    @staticmethod
    def retrieve_by_operator_id(operator_id):
        Manager.check_none(operator_id=operator_id)
        return Restaurant.query.filter(Restaurant.owner_id==operator_id).first()

    @staticmethod
    def retrieve_by_restaurant_name(restaurant_name):
        Manager.check_none(restaurant_name=restaurant_name)
        return Restaurant.query.filter(Restaurant.name==restaurant_name)

    @staticmethod
    def retrieve_by_restaurant_city(restaurant_city):
        Manager.check_none(restaurant_city=restaurant_city)
        return Restaurant.query.filter(Restaurant.city == restaurant_city)

    @staticmethod
    def retrieve_all():
        return Restaurant.query.all()

    @staticmethod
    def update_restaurant(restaurant: Restaurant):
        Manager.update(restaurant=restaurant)

    @staticmethod
    def delete_restaurant(restaurant: Restaurant):
        Manager.delete(restaurant=restaurant)

    @staticmethod
    def delete_restaurant_by_id(id_: int):
        restaurant = RestaurantManager.retrieve_by_id(id_)
        RestaurantManager.delete_restaurant(restaurant)
