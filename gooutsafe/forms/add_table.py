import wtforms as f
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class TableForm(FlaskForm):
    number = f.IntegerField('number', validators=[DataRequired()])
    max_capacity = f.IntegerField('max capacity', validators=[DataRequired()])
    display = ['number', 'max_capacity']
