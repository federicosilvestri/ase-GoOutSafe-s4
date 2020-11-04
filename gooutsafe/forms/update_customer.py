import wtforms as f
from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField, TelField
from wtforms.validators import DataRequired


class UpdateCustomerForm(FlaskForm):
    email = EmailField(
        'email',
        validators=[DataRequired()]
    )

    password = f.PasswordField(
        'password',
        validators=[DataRequired()]
    )

    phone = TelField(
        'phone',
        validators=[DataRequired()]
    )

    display = ['email', 'password', 'phone']
