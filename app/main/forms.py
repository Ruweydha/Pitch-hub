from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField("Tell us something about yourself", validators=[DataRequired()])
    submit = SubmitField('Submit')

class PitchesForm(FlaskForm):

    title = StringField('Pitch title', validators=[DataRequired()])
    content = TextAreaField('Write your pitch', validators=[DataRequired()])
    submit = SubmitField('Submit')    