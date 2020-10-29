import wtforms as f
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class ReservationForm(FlaskForm):

    start_time = f.TimeField('start_time', validators=[DataRequired()])
    end_time = f.TimeField('end_time', validators=[DataRequired()])
    people_number = f.IntegerField('people_number', validators=[DataRequired()])
    display = ['start_time', 'end_time']
