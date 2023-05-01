from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField 
from wtforms.validators import DataRequired, Length, ValidationError


class ResultForm(FlaskForm):
	roll_no = StringField('Enter Roll', validators=[DataRequired(), Length(min=8, max=25)])
	submit = SubmitField('Submit')

