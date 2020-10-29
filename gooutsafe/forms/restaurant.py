import wtforms as f
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class RestaurantForm(FlaskForm):
    list_menu = ['Italian', 'Japanese', 'Chinese','Mexican','American', 'Vegan', 'Vegeterian']

    name = f.StringField('name', validators=[DataRequired()])
    address = f.StringField('address', validators=[DataRequired()])
    city = f.StringField('city', validators=[DataRequired()])
    phone = f.StringField('phone', validators=[DataRequired()])
    menu_type = f.SelectField('menu_type', choices=list_menu, default=1)

    display = ['name', 'address', 'city', 'phone', 'menu_type']
