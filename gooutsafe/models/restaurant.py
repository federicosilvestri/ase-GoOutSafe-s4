from gooutsafe import db


class Restaurant(db.Model):
    __tablename__ = 'Restaurant'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text(100))
    likes = db.Column(db.Integer)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    phone = db.Column(db.Integer)
