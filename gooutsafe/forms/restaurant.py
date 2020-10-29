import wtforms as f
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class RestaurantForm(FlaskForm):
    list_menu = ['Italian', 'Japanese', 'Cinese','Mexican','American', 'Vegan', 'Vegeterian']

    name = f.StringField('name', validators=[DataRequired()])
    address = f.StringField('address', validators=[DataRequired()])
    city = f.StringField('city', validators=[DataRequired()])
    phone = f.StringField('phone', validators=[DataRequired()])
    menu_type = f.SelectField('menu_type', choices=list_menu, default=1)
    #start_time = f.TimeField('start_time', validators=[DataRequired()])
    #end_time = f.TimeField('end_time', validators=[DataRequired()])

    display = ['name', 'address', 'city', 'phone', 'menu_type']
