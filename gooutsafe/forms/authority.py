import wtforms as f
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class AuthorityForm(FlaskForm):
    list_choices = ['SSN', 'Email', 'Phone']

    track_type = f.SelectField('Type of tracking', choices=list_choices, default=1)
    customer_ident = f.StringField('Customer SSN/email/phone', validators=[DataRequired()])
