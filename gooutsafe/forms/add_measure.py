import wtforms as f
from flask_wtf import FlaskForm


class MeasureForm(FlaskForm):
    list_measure = ["Hand sanitizer", "Plexiglass", "Spaced tables",
                    "Sanitized rooms", "Temperature scanners"]
    measure = f.SelectField('Measure', choices=list_measure, default=1)
    display = ['measure']
