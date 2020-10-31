import wtforms as f
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    social_number = f.StringField('social_number', validators=[DataRequired()])
    email = f.StringField('email', validators=[DataRequired()])
    firstname = f.StringField('firstname', validators=[DataRequired()])
    lastname = f.StringField('lastname', validators=[DataRequired()])
    password = f.PasswordField('password', validators=[DataRequired()])
    dateofbirth = f.DateField('dateofbirth', format='%d-%m-%Y')
    phone = f.StringField('phone', validators=[DataRequired()])
    display = ['social_number','email', 'firstname', 'lastname', 'password', 
                'dateofbirth', 'phone']
