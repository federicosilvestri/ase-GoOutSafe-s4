from gooutsafe import db

class Role(db.Model):
    __tablename__ = 'Role'

    id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    name = db.Column(db.String(128), unique=True)

    def __init__(self, name):
        self.name = name
