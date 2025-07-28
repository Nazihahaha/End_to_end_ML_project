from flask_wtf import FlaskForm
import pandas as pd
from wtforms import (SelectField, DateField)
from wtforms.validators import DataRequired

train = pd.read_csv("data/train.csv")
val = pd.read_csv("data/val.csv")
X_data = pd.concat([train, val], axis=0).drop(columns="price")


class InputeForm(FlaskForm):
    airline = SelectField(label="Airline",
                          choices = X_data.airline.unique().tolist()
                          validators = [DataRequired()]
                          )
    date_of_journey = DateField(
        label="Date of Journey",
        validators=[DataRequired()]
    )
    source = SelectField(
        label = "Source"
        choices= X_data.source.unique().tolist()
        validators = [DataRequired()]
    )
    destination = SelectField(
        label = "Destination"
        choices= X_data.destination.unique().tolist()
        validators = [DataRequired()]
    )