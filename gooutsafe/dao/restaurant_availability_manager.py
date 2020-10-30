from .manager import Manager
from gooutsafe.models.restaurant_availability import RestaurantAvailability
from gooutsafe.models.restaurant import Restaurant


class RestaurantAvailabilityManager(Manager):

    @staticmethod
    def create_availability(ava: RestaurantAvailability):
        Manager.create(availability=ava)

    @staticmethod
    def retrieve_by_restaurant_id(restaurant_id):
        Manager.check_none(restaurant_id=restaurant_id)
        return RestaurantAvailability.query.filter(Restaurant.owner_id==restaurant_id).first()

    @staticmethod
    def delete_availabilitie(ava: RestaurantAvailability):
        Manager.delete(availability=ava)

    @staticmethod
    def update_availability(ava: RestaurantAvailability):
        Manager.update(availability=ava)