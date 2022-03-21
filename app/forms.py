from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, IntegerField
from wtforms.validators import InputRequired, Length, DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

#title, number of bedrooms, number of bathrooms,location and price.
class UploadForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    bedrooms = IntegerField('Bedrooms', validators=[DataRequired()])
    bathrooms =  IntegerField('Bathrooms', validators=[DataRequired()])

    location = StringField('Location', validators=[DataRequired()])
    price = IntegerField('Bathrooms', validators=[DataRequired()])
    type = SelectField('Type', choices=[('house', 'House'),('apartment','Apartment')], validators=[InputRequired()])

    description = TextAreaField('Description', validators=[DataRequired(), Length(min=10, max=1000, message="Write a description of the property.")])
    
    upload = FileField('photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])

