# type: ignore
from flask import current_app
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, SelectField, HiddenField, DateField
from wtforms.validators import InputRequired, length, EqualTo, ValidationError
from ..models import UserLogin, Employee
from dateutil import parser


class NewUserForm(FlaskForm):

    user_name = StringField("User Name", validators=[InputRequired(), length(min=2, max=20)])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[InputRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField("Create User")


    def validate_user_name(self, user_name):
        name = UserLogin.query.filter_by(user_name=user_name.data).first()

        if name:
            raise ValidationError("This User Name is already exist. Please choose another one")




class NewEmployeeForm(FlaskForm):
     # user_id = StringField("User ID", validators=[InputRequired()])
    employee_id = StringField("User ID", validators=[InputRequired(), length(min=1, max=6)])
    employee_name = StringField("User Name", validators=[InputRequired(), length(min=2, max=20)])
    #update the user department to be a string field based on the drop down list came from front end to be more simple and scalable
    employee_department = SelectField("User Department", choices=["", "Accountant", "Operation", "HR", "IT", "Admin", "Stock Control", "Supply Chain", "Quality Control"], validators=[InputRequired()], validate_choice=True)
    #user_department = SelectField("User Department", choices=["IT", "Accountant", "HR", "Operation", "Supply Chain", "Stock Control", "Admin", "Quality Control"])
    
    #update the user job to be a string field based on the drop down list came from front end to be more simple and scalable
    # user_job = StringField("User Job Title", validators=[InputRequired(), length(min=2, max=20)])
    employee_job_title = SelectField("User Job Title", choices=["", "Web Developer", "Accountant", "HR Generalist", "Team Leader", "Section head"], validate_choice=True, validators=[InputRequired()] )

    employee_branch = SelectField("User Branch", choices=["", "Head Quarter", "Heliopolis", "Nasr City", "New Cairo", "6th October"], validate_choice=True, validators=[InputRequired()] )
    submit = SubmitField("Add Employee")


    def validate_employee_id(self, employee_id):
        id = Employee.query.filter_by(employee_id=employee_id.data).first()
        
        if id:
            raise ValidationError("This User ID is already exist. Please choose another one")
        

        

    def validate_user_name(self, employee_name):
        name = Employee.query.filter_by(employee_name=employee_name.data).first()

        if name:
            raise ValidationError("This User Name is already exist. Please choose another one")


class SearchAttendanceDate(FlaskForm):
    start_date = DateField("From", format="%Y-%m-%d", validators=[InputRequired(message="You have to insert starting date")])
    end_date = DateField("To", format="%Y-%m-%d", validators=[InputRequired(message="You have to insert ending date")])
    submit = SubmitField("Search")

    def validate_start_date(self, start_date):
        date_format = "%d-%m-%Y"
        if not parser.parse(start_date.data):
            raise ValidationError(f"The date format must be in form: {date_format}.")
        
    def validate_end_date(self, end_date):
        date_format = "%d-%m-%Y"
        if not parser.parse(end_date.data):
            raise ValidationError(f"The date format must be in form: {date_format}.")

        