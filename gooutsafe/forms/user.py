import wtforms as f
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField, EmailField, TelField
from wtforms.validators import DataRequired

import datetime


class UserForm(FlaskForm):
    social_number = f.StringField(
        'Social Number',
        validators=[DataRequired()]
    )

    email = EmailField(
        'Email',
        validators=[DataRequired()]
    )

    firstname = f.StringField(
        'Firstname',
        validators=[DataRequired()]
    )

    lastname = f.StringField(
        'Lastname',
        validators=[DataRequired()]
    )

    password = f.PasswordField(
        'Password',
        validators=[DataRequired()]
    )

    birthdate = DateField(
        'Birthday'
    )

    phone = TelField(
        'Phone',
        validators=[DataRequired()]
    )

    def validate_on_submit(self):
        result = super(UserForm, self).validate()
        this_year = datetime.date.today().year
        if this_year - self.birthdate.data.year < 18:
            return False
        else:
            return result

    display = ['social_number', 'email', 'firstname', 'lastname', 'password',
               'birthdate', 'phone']
