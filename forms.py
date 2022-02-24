from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SelectField, SubmitField, RadioField, validators, DateField
from wtforms.validators import DataRequired

class ChoiceForm(FlaskForm):

    submit = SubmitField("Submit Answer")
    
    # questions:
    # How many states of the United States? : 49, 30, 50, 13
    # Which is the only continent where spiders don’t exist? antarctica, north america, africa, australia
    # What is the capital of France? LONDON, new York, Paris, Moscow?
    # Which is the largest U.S state? Alaska, Hawaii, Arizona, Texas?
    # Which is the smallest planet in the solar system? Mercury, Pluto, Venus, Mars

