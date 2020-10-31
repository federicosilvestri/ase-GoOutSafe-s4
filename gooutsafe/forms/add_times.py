import wtforms as f
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class TimesForm(FlaskForm):
    start_time = f.TimeField('start_time', validators=[DataRequired()])
    end_time = f.TimeField('end_time', validators=[DataRequired()])
    display = ['start_time', 'end_time']


#TODO input a tendina o orologio