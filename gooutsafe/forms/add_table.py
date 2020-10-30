import wtforms as f
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class TableForm(FlaskForm):
    number = f.IntegerField('number', validators=[DataRequired()])
    capacity = f.IntegerField('capacity', validators=[DataRequired()])
    display = ['number', 'capacity']
