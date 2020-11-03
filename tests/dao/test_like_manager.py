from .dao_test import DaoTest


class TestLikeManager(DaoTest):

    @classmethod
    def setUpClass(cls):
        super(TestLikeManager, cls).setUpClass()
        from gooutsafe.dao import like_manager
        cls.like_manager = like_manager

    def test_crud(self):
        # @TODO we need RestaurantManager
        pass
