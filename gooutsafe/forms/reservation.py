import wtforms as f
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField, DateTimeField, TimeField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from wtforms.widgets.html5 import TimeInput
from datetime import datetime, timedelta, time


class ReservationForm(FlaskForm):

    start_date = DateField('Date', validators=[DataRequired()])
    start_time = TimeField('Time', validators=[DataRequired()])
    people_number = IntegerField('Number of Peoples', validators=[NumberRange(min=1, max=20), DataRequired()])
    display = ['start_date', 'start_time', 'people_number']
    