from .auth import auth
from .home import home
from .restaurants import restaurants
from .users import users
from .table import table
from .reservation import reservation
from .health_authority import authority
from .review import review

blueprints = [home, auth, users, restaurants, table, reservation, authority, review]
