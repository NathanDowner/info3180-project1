from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed


class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[InputRequired()])
    lname = StringField('Last Name', validators=[InputRequired()])
    gender = SelectField('Gender', choices=[
        ('Female','Male'),('Female','Female')], 
        validators=[InputRequired()
    ])
    email = StringField('Email', validators=[InputRequired(), Email()])
    location = StringField('Location', validators=[InputRequired()])
    bio = TextAreaField('Biography', validators=[InputRequired()])
    image = FileField('Image', validators=[
        FileRequired(), 
        FileAllowed(['jpg','png'], 'Images only!')
    ])
    
