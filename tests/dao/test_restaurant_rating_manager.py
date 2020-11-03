from .dao_test import DaoTest


class RestaurantRatingManagerTest(DaoTest):
    
    @classmethod
    def setUpClass(cls):
        super(RestaurantRatingManagerTest, cls).setUpClass()

        from gooutsafe.dao.restaurant_rating_manager import RestaurantRating
        cls.restaurant_rating_manager = RestaurantRating

    def test_create_delete(self):
        """
        @TODO it will be implemented when restaurant dao will be done
        :return:
        """
        pass
