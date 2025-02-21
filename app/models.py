# type: ignore

# the statement above ^^ "# type: ignore" is necessary to ignore the Mypy type checker error

# This model is for creating the database and tables using AQLALCHEMY Database configuered in the config.py file

from sqlalchemy.sql.expression import func
from sqlalchemy import text, Index
#from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone, time, date
#from . import login_manager

# from flask_bcrypt import Bcrypt 
# from flask_sqlalchemy import SQLAlchemy

from app import db




#class UserLogin(UserMixin, db.Model):
class UserLogin(db.Model):
    """ A table contain all authinticated users and their hashed passwords"""
    __tablename__ = "user_login"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), nullable=False, unique=True)
    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


#class Employee(UserMixin, db.Model):

class Employee (db.Model):
    """ A table contains employees' data """
    __tablename__ = "employees"

    __table_args__ = {'extend_existing': True}

    employee_id = db.Column(db.String(6), nullable=False, primary_key=True)
    employee_name = db.Column(db.String(20), nullable=False, unique=True)
    employee_department = db.Column(db.String(20), nullable=False)
    employee_job_title = db.Column(db.String(20), nullable=False)
    branch = db.Column(db.String(30), nullable=False)
    employee_attendance = db.relationship("Attendance", backref="employee", lazy="dynamic")

class Attendance(db.Model):
    """ A table that contains all employees' attendance """
    __tablename__ = "attendance"

    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(6), db.ForeignKey("employees.employee_id"), nullable=False)
    check_in_time = db.Column(db.Time, nullable=False)  
    check_out_time = db.Column(db.Time, nullable=False) 
    total_hours = db.Column(db.Float, nullable=False)  
    overtime_hours = db.Column(db.Float, default=0.0)  
    delay_penalty = db.Column(db.Float, default=0.0)  
    date = db.Column(db.Date, nullable=False) 


class Machine(db.Model):
    """ A table that contains fingerprint machines data """
    __tablename__ = "machines"

    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.Integer, autoincrement=True)
    machine_location = db.Column(db.String(30), nullable=False)
    machine_ip = db.Column(db.String(30), nullable=False, unique=True)


