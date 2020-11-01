from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField, TimeField, IntegerField
from wtforms.validators import DataRequired, NumberRange
<<<<<<< HEAD
from wtforms.widgets.html5 import TimeInput
from datetime import datetime, timedelta, time
=======
from datetime import datetime
>>>>>>> e0e64796457d07549153a3f6ed13b349e9b86cbd


class ReservationForm(FlaskForm):

<<<<<<< HEAD
    start_date = DateField('Date', validators=[DataRequired()])
    start_time = TimeField('Time', validators=[DataRequired()])
    people_number = IntegerField('Number of Peoples', validators=[NumberRange(min=1, max=20), DataRequired()])
=======
    start_date = DateField(
        'Date',
        format='%Y-%m-%d',
        default=datetime.now(),
        validators=[DataRequired()]
    )

    start_time = TimeField(
        'Time',
        format='%H-%M',
        default=datetime.now(),
        render_kw={"step": "1"},
        validators=[DataRequired()]
    )

    people_number = IntegerField(
        'Number of Peoples',
        default=1,
        validators=[
            DataRequired(),
            NumberRange(min=1, max=20)]
    )

>>>>>>> e0e64796457d07549153a3f6ed13b349e9b86cbd
    display = ['start_date', 'start_time', 'people_number']
    