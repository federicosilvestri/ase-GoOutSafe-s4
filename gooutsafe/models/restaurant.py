from gooutsafe import db


class Restaurant(db.Model):
    __tablename__ = 'Restaurant'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # TODO: add owner relationship when its model is created
    name = db.Column(db.Text(100))
    likes = db.Column(db.Integer)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    phone = db.Column(db.Integer)
    menu_type = db.Column(db.Text(100))
    is_open = db.Column(db.Boolean, default=False)
    # TODO: add ratings relationship when their model is created
    # TODO: add availability relationship when their model is created

    def __init__(self, name, lat, lon, phone, menu_type):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.phone = phone
        self.menu_type = menu_type
