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

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # TODO: add owner relationship when its model is created
    name = db.Column(db.Text(MAX_NAME_LENGTH))
    likes = db.Column(db.Integer) # obsolete
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    phone = db.Column(db.Integer)
    menu_type = db.Column(db.Text(MAX_MENU_TYPE_LENGTH))
    is_open = db.Column(db.Boolean, default=False)
    # TODO: add ratings relationship when their model is created
    # TODO: add availability relationship when their model is created


    def __init__(self, name, lat, lon, phone, menu_type):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.phone = phone
        self.menu_type = menu_type
        self.is_open = False

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if len(name) <= self.MAX_NAME_LENGTH and len(name) > 0:
            self.__name = name
        else:
            raise ValueError("Invalid restaurant name length")
    
    @property
    def lat(self):
        return self.__lat
    
    @lat.setter
    def lat(self, lat):
        if lat >= self.MIN_LAT and lat <= self.MAX_LAT:
            self.__lat = lat
        else:
            raise ValueError("Invalid latitude value")

    @property
    def lon(self):
        return self.__lon

    @lon.setter
    def lon(self, lon):
        if lon >= self.MIN_LON and lon <= self.MAX_LON:
            self.__lon = lon
        else:
            raise ValueError("Invalid longitude value")

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if phone >= self.MIN_PHONE_VALUE and phone <= self.MAX_PHONE_VALUE:
            self.__phone = phone
        else:
            raise ValueError("Invalid phone number")
    
    @property
    def menu_type(self):
        return self.__menu_type
    
    @menu_type.setter
    def menu_type(self, menu_type):
        if len(menu_type) > 0 and len(menu_type) <= self.MAX_MENU_TYPE_LENGTH:
            self.__menu_type = menu_type
        else:
            raise ValueError("Invalid menu type")

    @property
    def is_open(self):
        return self.__is_open
    
    @is_open.setter
    def is_open(self, is_open):
        self.__is_open = is_open