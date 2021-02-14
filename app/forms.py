from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length

class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=5, max=64)])
    description = StringField('Description', validators=[Length(max=200)])
    price = DecimalField('Price', validators=[DataRequired()])
    photo_url = StringField('Photo')
    submit = SubmitField('Add Product')