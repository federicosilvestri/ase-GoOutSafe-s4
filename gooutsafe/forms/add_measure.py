import wtforms as f
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class MeasureForm(FlaskForm):
    measure = f.StringField('Measure', validators=[DataRequired()])
    display = ['measure']
