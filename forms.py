from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, URLField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange


class AddPetForm(FlaskForm):
    """Form for adding new pets"""

    name = StringField("Pet Name", [InputRequired()])
    species = SelectField(
        "Species", choices=[("dog", "Dog"), ("cat", "Cat"), ("alpaca", "Alpaca")]
    )
    photo_url = URLField("Photo URL", [Optional()])
    age = IntegerField("Age", [Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes", [Optional()])


class EditPetForm(FlaskForm):
    """Form for editing existing pets"""

    photo_url = URLField("Photo URL", [Optional()])
    notes = StringField("Notes", [Optional()])
    available = BooleanField("Available", [Optional()])
