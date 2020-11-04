from .dao_test import DaoTest
from tests.models.test_like import TestLike


class TestLikeManager(DaoTest):

    @classmethod
    def setUpClass(cls):
        super(TestLikeManager, cls).setUpClass()
        from gooutsafe.dao import like_manager
        cls.like_manager = like_manager

    def test_crud(self):
        pass

        """
    @staticmethod
    def create_like(user_id, restaurant_id):
        like = Like(
            user_id=user_id,
            restaurant_id=restaurant_id
        )
        Manager.create(like=like)

    @staticmethod
    def get_like_by_id(user_id, restaurant_id):
        like = Like.query.get(user_id, restaurant_id)
        return like

        """