from gooutsafe import db
from gooutsafe.models.user import User
from gooutsafe.dao.manager import Manager


class UserManager(Manager):

    @staticmethod
    def create_user(user: User):
        Manager.check_none(user=user)

        db.session.add(user)
        db.session.commit()

    @staticmethod
    def retrieve(id):
        Manager.check_none(id=id)
        return User.query.get(id)

    @staticmethod
    def update_user(user: User):
        Manager.check_none(user=user)

    @staticmethod
    def delete_user(user: User):
        Manager.check_none(user=user)
        db.session.delete(user)
        db.session.commit()





