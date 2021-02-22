from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length, ValidationError
from app.models import Product

class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=5, max=64)])
    description = StringField('Description', validators=[Length(max=200)])
    price = DecimalField('Price', validators=[InputRequired()])
    photo_url = FileField('Photo', validators=[FileAllowed(['jpg', 'png'], "wrong format!")])
    submit = SubmitField('Add Product')

    def validate_name(self, name):
        product = Product.query.filter_by(name=name.data).first()
        if product:
            raise ValidationError("A product with that name already exists!")