from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email, Length
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
    bio = TextAreaField('Biography', validators=[
        InputRequired(),
        Length(min=10, max=1000, message="Must enter at least 10 characters.")
    ])
    image = FileField('Image', validators=[
        FileRequired("You need a profile pic."), 
        FileAllowed(['jpg','png'], 'Images only!')
    ])
    
