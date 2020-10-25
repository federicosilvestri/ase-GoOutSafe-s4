from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

"""
This is the main db object for the project, 
it will be used by all beans.
"""
db = SQLAlchemy()
migrate = Migrate()
