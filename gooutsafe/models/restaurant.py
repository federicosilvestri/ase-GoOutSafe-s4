from gooutsafe import db


class Restaurant(db.Model):
    __tablename__ = 'Restaurant'

    #### CONSTANTS ####
    MAX_NAME_LENGTH = 100
    # taken from Google Maps bounds
    MAX_LAT = 85
    MIN_LAT = -85
    MAX_LON = 180
    MIN_LON = -180
    # based on italian phone numbers, composed by 10 digits
    # (TODO needs better lower bound)
    MAX_PHONE_VALUE = 9999999999
    MIN_PHONE_VALUE = 0
    MAX_MENU_TYPE_LENGTH = 100

    __id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # TODO: add owner relationship when its model is created
    __name = db.Column(db.Text(MAX_NAME_LENGTH))
    __likes = db.Column(db.Integer)  # obsolete
    __lat = db.Column(db.Float)
    __lon = db.Column(db.Float)
    __phone = db.Column(db.Integer)
    __menu_type = db.Column(db.Text(MAX_MENU_TYPE_LENGTH))
    __is_open = db.Column(db.Boolean, default=False)

    # TODO: add ratings relationship when their model is created
    # TODO: add availability relationship when their model is created

    def __init__(self, name, lat, lon, phone, menu_type):
        self.__name = name
        self.__lat = lat
        self.__lon = lon
        self.__phone = phone
        self.__menu_type = menu_type
        self.__is_open = False


    def get_id (self):
        return self.__id
        
    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) <= self.MAX_NAME_LENGTH and len(name) > 0:
            self.__name = name
        else:
            raise ValueError("Invalid restaurant name length")

    def get_lat(self):
        return self.__lat

    def set_lat(self, lat):
        if lat >= self.MIN_LAT and lat <= self.MAX_LAT:
            self.__lat = lat
        else:
            raise ValueError("Invalid latitude value")

    def get_lon(self):
        return self.__lon

    def set_lon(self, lon):
        if lon >= self.MIN_LON and lon <= self.MAX_LON:
            self.__lon = lon
        else:
            raise ValueError("Invalid longitude value")


    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        if phone >= self.MIN_PHONE_VALUE and phone <= self.MAX_PHONE_VALUE:
            self.__phone = phone
        else:
            raise ValueError("Invalid phone number")

    def get_menu_type(self):
        return self.__menu_type

    def set_menu_type(self, menu_type):
        if len(menu_type) > 0 and len(menu_type) <= self.MAX_MENU_TYPE_LENGTH:
            self.__menu_type = menu_type
        else:
            raise ValueError("Invalid menu type")

    def get_is_open(self):
        return self.__is_open

    def set_is_open(self, is_open):
        self.__is_open = is_open
