from gooutsafe import db
from .user import User
from sqlalchemy.orm import relationship


class Customer(User):

    SOCIAL_CODE_LENGTH = 16

    __tablename__ = 'Customer'

    id = db.Column(db.Integer, db.ForeignKey('User.id', ondelete="CASCADE"), primary_key=True)
    firstname = db.Column(db.Unicode(128))
    lastname = db.Column(db.Unicode(128))
    birthday = db.Column(db.DateTime)
    social_number = db.Column(db.Unicode(SOCIAL_CODE_LENGTH))
    health_status = db.Column(db.Boolean, default=False)
    likes = relationship('Like', back_populates='liker')

    __mapper_args__ = {
        'polymorphic_identity': 'customer',
    }

    def __init__(self, *args, **kw):
        super(Customer, self).__init__(*args, **kw)
        self._authenticated = False

    def set_firstname(self, name):
        self.firstname = name

    def set_lastname(self, name):
        self.lastname = name

    def set_birthday(self, birthday):
        self.birthday = birthday

    def set_health_status(self, status):
        self.health_status = status
    
    @staticmethod
    def check_social_number(social_number):
        if len(social_number) != Customer.SOCIAL_CODE_LENGTH:
            raise ValueError("Invalid Social Number length")

    def set_social_number(self, social_number):
        Customer.check_social_number(social_number)
        self.social_number = social_number
