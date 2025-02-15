# type: ignore

# the statement above ^^ "# type: ignore" is necessary to ignore the Mypy type checker error

# This model is for creating the database and tables using AQLALCHEMY Database configuered in the config.py file

from sqlalchemy.sql.expression import func
from sqlalchemy import text, Index
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone
#from . import login_manager

# from flask_bcrypt import Bcrypt 
# from flask_sqlalchemy import SQLAlchemy

from app import db

# db = SQLAlchemy()
# bcrypt = Bcrypt()



class UserLogin(UserMixin, db.Model):
    """ A table contain all authinticated users and their hashed passwords"""
    __tablename__ = "user_login"
    __table_args__ = {'extend_existing': True}

    user_name = db.Column(db.String(20), nullable=False, unique=True)
    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Employee(UserMixin, db.Model):
    """ A table contains employees' data """
    __tablename__ = "employees"

    __table_args__ = {'extend_existing': True}

    employee_id = db.Column(db.String(6), nullable=False, primary_key=True)
    employee_name = db.Column(db.String(20), nullable=False, unique=True)
    employee_department = db.Column(db.String(20), nullable=False)
    employee_job_title = db.Column(db.String(20), nullable=False)
    branch = db.Column(db.String(30), nullable=False)
    employee_attendance = db.relationship("Attendance", backref="employee", lazy=True)


class Attendance(db.Model):
    """ A table that contains all employees' attendance """
    __tablename__ = "attendance"

    __table_args__ = {'extend_existing': True}


    #submission_date = db.Column(db.Date, nullable=False, default=func.now().cast(db.Date))
    # submission_date = db.Column(db.Date, nullable=True, default=func.now().cast(db.Date))

    submission_datetime = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc))

    #submission_time = db.Column(db.Time, nullable=False, default=text("TIME(CURRENT_TIMESTAMP)"))
    # submission_time = db.Column(db.Time, nullable=True, default=text("TIME(CURRENT_TIMESTAMP)"))

    # submission_time = db.Column(db.String(15), nullable=False)


    employee = db.Column(db.String(6), db.ForeignKey("employee.employee_id"))


class Machine(db.Model):
    """ A table that contains fingerprint machines data """
    __tablename__ = "machines"

    __table_args__ = {'extend_existing': True}

    index = db.Column(db.Integer, autoincrement=True)
    machine_location = db.Column(db.String(30), nullable=False)
    machine_ip = db.Column(db.String(30), nullable=False, unique=True)


