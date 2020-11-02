import wtforms as f
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class HomeForm(FlaskForm):
    restaurant_filters = ['Name', 'City']
    search_field = f.StringField('Search Field')
    filters = f.SelectField('Search By', choices=restaurant_filters, default=1)


    


