from .dao_test import DaoTest


class TestLikeManager(DaoTest):

    def setUp(self):
        super(TestLikeManager, self).setUp()

        from gooutsafe.dao import like_manager

        self.like_manager = like_manager

    def test_crud(self):
        # @TODO we need RestaurantManager
        pass
