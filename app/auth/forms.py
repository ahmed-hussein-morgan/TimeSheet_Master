# type: ignore
from flask import current_app
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, BooleanField, EmailField, SelectField, TextAreaField, IntegerField
from wtforms.validators import InputRequired, length, Email, EqualTo, DataRequired, ValidationError
from ..models import UserLogin, Employee, Attendance, Machine



class LoginForm(FlaskForm):
    user_name = StringField('User Name', validators=[InputRequired(), length(max=18)])
    password = PasswordField('Password', validators=[InputRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
