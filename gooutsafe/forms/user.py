import wtforms as f
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField, EmailField, TelField
from wtforms.validators import DataRequired

import datetime


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

    def validate_on_submit(self):
        result = super(UserForm, self).validate()
        this_year = datetime.date.today().year
        if this_year - self.birthdate.data.year < 18:
            return False
        else:
            return result

    display = ['social_number', 'email', 'firstname', 'lastname', 'password',
               'birthdate', 'phone']
