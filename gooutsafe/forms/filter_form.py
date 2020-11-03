from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField, TimeField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from wtforms.widgets.html5 import TimeInput
from datetime import datetime, timedelta, time

import datetime


class FilterForm(FlaskForm):

    filter_date = DateField('Filter Date')