from gooutsafe.dao.manager import Manager
from gooutsafe.models.like import Like


class LikeManager(Manager):

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
    
