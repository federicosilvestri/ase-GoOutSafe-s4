from gooutsafe import db
from sqlalchemy.orm import relationship


class Restaurant(db.Model):
    __tablename__ = 'Restaurant'

    MAX_NAME_LENGTH = 100
    # taken from Google Maps bounds
    MAX_LAT = 85
    MIN_LAT = -85
    MAX_LON = 180
    MIN_LON = -180
    MAX_PHONE_LEN = 15
    MAX_MENU_TYPE_LENGTH = 100

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # TODO: add owner relationship when its model is created
    name = db.Column(db.String(
        length=MAX_NAME_LENGTH
    ))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    phone = db.Column(db.String(
        length=MAX_PHONE_LEN
    ))
    menu_type = db.Column(db.String(
        length=MAX_MENU_TYPE_LENGTH
    ))
    is_open = db.Column(
        db.Boolean, default=False
    )
    tables = relationship("Table")

    # TODO: add ratings relationship when their model is created
    # TODO: add availability relationship when their model is created
    # TODO: add hybrid property or method to calculate the number of likes

    def __init__(self, name, lat, lon, phone, menu_type):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.phone = phone
        self.menu_type = menu_type
        self.is_open = False

    def set_name(self, name):
        if self.MAX_NAME_LENGTH >= len(name) > 0:
            self.name = name
        else:
            raise ValueError("Invalid restaurant name length")

    def set_lat(self, lat):
        if self.MIN_LAT <= lat <= self.MAX_LAT:
            self.lat = lat
        else:
            raise ValueError("Invalid latitude value")

    def set_lon(self, lon):
        if self.MIN_LON <= lon <= self.MAX_LON:
            self.lon = lon
        else:
            raise ValueError("Invalid longitude value")

    def set_phone(self, phone):
        if self.MIN_PHONE_VALUE <= phone <= self.MAX_PHONE_VALUE:
            self.phone = phone
        else:
            raise ValueError("Invalid phone number")

    def set_menu_type(self, menu_type):
        if 0 < len(menu_type) <= self.MAX_MENU_TYPE_LENGTH:
            self.menu_type = menu_type
        else:
            raise ValueError("Invalid menu type")

    def set_is_open(self, is_open):
        self.is_open = is_open
