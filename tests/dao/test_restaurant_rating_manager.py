from .dao_test import DaoTest


class RestaurantRatingManagerTest(DaoTest):
    
    def setUp(self):
        super(RestaurantRatingManagerTest, self).setUp()

        from gooutsafe.dao.restaurant_rating_manager import RestaurantRating
        self.restaurant_rating_manager = RestaurantRating

    def test_create_delete(self):
        """
        @TODO it will be implemented when restaurant dao will be done
        :return:
        """
        pass
