import wtforms as f
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField, EmailField, TelField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    social_number = f.StringField(
        'social_number',
        validators=[DataRequired()]
    )

    email = EmailField(
        'email',
        validators=[DataRequired()]
    )

    firstname = f.StringField(
        'firstname',
        validators=[DataRequired()]
    )

    lastname = f.StringField(
        'lastname',
        validators=[DataRequired()]
    )

    password = f.PasswordField(
        'password',
        validators=[DataRequired()]
    )

    birthdate = DateField(
        'birthday'
    )

    phone = TelField(
        'phone',
        validators=[DataRequired()]
    )

    display = ['social_number', 'email', 'firstname', 'lastname', 'password',
               'birthdate', 'phone']
