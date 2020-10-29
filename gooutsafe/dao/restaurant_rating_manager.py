from gooutsafe.dao.manager import Manager
from gooutsafe.models.restaurant_rating import RestaurantRating


class RestaurantRatingManager(Manager):
    """
    List of ratings are implemented
    in the Restaurant DAO and User DAO
    """

    @staticmethod
    def create_rating(rating: RestaurantRating):
        Manager.create(rating=rating)

    @staticmethod
    def delete_rating(rating: RestaurantRating):
        Manager.delete(rating=rating)

    @staticmethod
    def update_rating(rating: RestaurantRating):
        Manager.update(rating=rating)
