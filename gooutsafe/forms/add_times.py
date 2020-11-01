import wtforms as f
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.fields.html5 import TimeField


def validate_start_time(form, field):
    if start_time > end_time:
        raise ValidationError('End time must be after start time')

class TimesForm(FlaskForm):
    start_time = TimeField('start time', 
        validators=[
            DataRequired(),
            validate_start_time
    ])
    end_time = TimeField('end time', 
        validators=[
            DataRequired()
    ])
    display = ['start_time', 'end_time']