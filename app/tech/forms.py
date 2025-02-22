# type: ignore
from flask import current_app
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, BooleanField, EmailField, SelectField, TextAreaField, IntegerField,HiddenField
from wtforms.validators import InputRequired, length, Email, EqualTo, DataRequired, ValidationError
from ..models import UserLogin, Employee, Attendance, Machine


class NewUserForm(FlaskForm):

    user_name = StringField("User Name", validators=[InputRequired(), length(min=2, max=20)])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[InputRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField("Create")


    def validate_user_name(self, user_name):
        name = UserLogin.query.filter_by(user_name=user_name.data).first()

        if name:
            raise ValidationError("This User Name is already exist. Please choose another one")




class NewEmployeeForm(FlaskForm):
    