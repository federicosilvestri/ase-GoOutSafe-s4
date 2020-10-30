import wtforms as f
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class ReservationForm(FlaskForm):

    start_date = f.DateField('Resevation Date', validators=[DataRequired()])
    start_time = f.TimeField('Reservation Time', validators=[DataRequired()])
    people_number = f.IntegerField('People Number', validators=[DataRequired()])
    #display = ['start_date', 'start_time', 'people_number']
