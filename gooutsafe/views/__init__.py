from .auth import auth
from .home import home
from .restaurants import restaurants
from .users import users
from .table import table
from .reservation import reservation

blueprints = [home, auth, users, restaurants, table, reservation]
