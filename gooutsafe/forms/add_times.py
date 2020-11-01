import wtforms as f
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.fields.html5 import TimeField


class TimesForm(FlaskForm):
    start_time = TimeField('start time', 
        validators=[
            DataRequired()
    ])
    end_time = TimeField('end time', 
        validators=[
            DataRequired()
    ])
    display = ['start_time', 'end_time']