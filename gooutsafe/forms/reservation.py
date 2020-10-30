import wtforms as f
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class ReservationForm(FlaskForm):

    start_date = f.DateField('Resevation Date', validators=[DataRequired()])
    #time_slots = f.SelectField('Time', choices=list_menu, default=1)
    people_number = f.IntegerField('Number of Peoples', validators=[DataRequired()])
    #display = ['start_date', 'start_time', 'people_number']
