from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email, Length, DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

#title, number of bedrooms, number of bathrooms,location and price.
class UploadForm(FlaskForm):


    upload = FileField('photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])

