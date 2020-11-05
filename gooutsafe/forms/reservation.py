import datetime
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField, TimeField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class ReservationForm(FlaskForm):
    start_date = DateField('Date', validators=[DataRequired()])
    start_time = TimeField('Time', validators=[DataRequired()])
    people_number = IntegerField('Number of Persons',
                                 validators=[
                                     NumberRange(min=1, max=20),
                                     DataRequired()
                                 ]
                                 )

    def validate_on_submit(self):
        result = super(ReservationForm, self).validate()
        date = self.start_date.data
        time = self.start_time.data
        people_number = self.people_number.data
        start_time_merged = datetime.combine(date, time)
        if start_time_merged < datetime.now() or people_number <= 0:
            return False
        else:
            return result

    display = ['start_date', 'start_time', 'people_number']
