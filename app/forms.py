from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed


class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[InputRequired('A name is required')])
    lname = StringField('Last Name', validators=[InputRequired('A name is required')])
    gender = SelectField('Gender', choices=[
        ('Female','Male'),('Female','Female')], 
        validators=[InputRequired()
    ])
    email = StringField('Email', validators=[InputRequired(), Email('Enter a valid email')])
    location = StringField('Location', validators=[InputRequired()])
    bio = TextAreaField('Biography', validators=[InputRequired()])
    image = FileField('Image', validators=[
        FileRequired(), 
        FileAllowed(['jpg','png'], 'Images only!')
    ])
    
