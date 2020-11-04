import wtforms as f
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.fields.html5 import TimeField


class TimesForm(FlaskForm):

    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

    day = f.SelectField('Week Day', choices = week_days, validators=[DataRequired()])
    start_time = TimeField('Start time', 
        validators=[
            DataRequired()
    ])
    end_time = TimeField('End time', 
        validators=[
            DataRequired()
    ])
    display = ['start_time', 'end_time']