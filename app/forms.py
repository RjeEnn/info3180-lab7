from flask_wtf import FlaskForm
from wtforms import StringField
from flask_wtf.file import FileAllowed, FileRequired, FileField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    description = StringField('Message', widget=TextArea(), validators=[DataRequired()])
    photo = FileField('Upload Image', validators=[FileRequired(), FileAllowed(['jpg', 'img', 'jpeg', 'png'], 'Please Upload a valid image type (jpg/png)')])