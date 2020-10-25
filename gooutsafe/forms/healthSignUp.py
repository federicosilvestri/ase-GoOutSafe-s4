import wtforms as f
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class HealthAuthForm(FlaskForm):
    email = f.StringField('email', validators=[DataRequired()])
    password = f.PasswordField('password', validators=[DataRequired()])
    name = f.StringField('name', validators=[DataRequired()])
    city = f.StringField('city', validators=[DataRequired()])
    address = f.StringField('address', validators=[DataRequired()])
    phone = f.StringField('phone', validators=[DataRequired()])
    display = ['email', 'password', 'name', 'city', 'address', 'phone']