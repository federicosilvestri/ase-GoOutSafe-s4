import wtforms as f
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class OperatorForm(FlaskForm):
    email = f.StringField('email', validators=[DataRequired()])
    password = f.PasswordField('password', validators=[DataRequired()])
    display = ['email', 'password']
