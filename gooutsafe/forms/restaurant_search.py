import wtforms as f
from flask_wtf import FlaskForm


class HomeForm(FlaskForm):
    restaurant_filters = ['Name', 'City', 'Menu Type']
    search_field = f.StringField('Search Field')
    filters = f.SelectField('Search By', choices=restaurant_filters, default=1)
