import wtforms as f
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = f.StringField(
        'email',
        validators=[DataRequired()],
        id="inputEmail",
    )
    password = f.PasswordField('password', validators=[DataRequired()])
    display = ['email', 'password']
