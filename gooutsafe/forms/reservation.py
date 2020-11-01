import wtforms as f
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField, DateTimeField, TimeField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from datetime import datetime, timedelta, time


class ReservationForm(FlaskForm):

    start_date = DateField('Date',format='%Y-%m-%d', default=datetime.now(), validators=[DataRequired()])
    start_time = TimeField('Time', format='%H-%M', default=datetime.now(), render_kw={"step": "1"}, validators=[DataRequired()])
    people_number = IntegerField('Number of Peoples', default=1, validators=[DataRequired(), NumberRange(min=1, max=20)])
    display = ['start_date', 'start_time', 'people_number']
    

