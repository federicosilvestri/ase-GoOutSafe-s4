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
    def update_restaurant(restaurant: Restaurant):
        Manager.update(restaurant=restaurant)

    @staticmethod
    def delete_restaurant(restaurant: Restaurant):
        Manager.delete(restaurant=restaurant)

    @staticmethod
    def delete_restaurant_by_id(id_: int):
        restaurant = RestaurantManager.retrieve_by_id(id_)
        RestaurantManager.delete_restaurant(restaurant)
