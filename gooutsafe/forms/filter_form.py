from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField, TimeField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from wtforms.widgets.html5 import TimeInput
from datetime import datetime, timedelta, time

import datetime


class FilterForm(FlaskForm):
    filter_date = DateField(default=datetime.date.today())
    start_time = TimeField(default=time(hour=0))
    end_time = TimeField(default=time(hour=23))

    display = ['filter_date', 'start_time', 'end_time']