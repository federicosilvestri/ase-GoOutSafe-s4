import wtforms as f
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from datetime import datetime, timedelta, time


class ReservationForm(FlaskForm):

    time_slot_init = ['00:00']

    start_date = f.DateField('Resevation Date', validators=[DataRequired()])
    time_slots = f.SelectField('Time', choices=time_slot_init, default=1)
    people_number = f.IntegerField('Number of Peoples', validators=[DataRequired()])
    display = ['start_date', 'time_slots', 'people_number']
    
    def __init__(self, time_slots):
        super().__init__() 
        self.time_slots.choices = time_slots


