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


class User(UserMixin, db.Model):
    """ A table containing employees data """
    __tablename__ = "employees"



    __table_args__ = {'extend_existing': True}


    id = db.Column(db.Integer, primary_key=True, nullable=False)
    employee_id = db.Column(db.Integer, unique=True, nullable=False)
    employee_name = db.Column(db.String(20), nullable=False, unique=True)
    department = db.Column(db.String(20), nullable=False)
    job_title = db.Column(db.String(20), nullable=False)

    role_type = db.Column(db.String(20), nullable=False)
    # role_type_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

    email = db.Column(db.String(64), nullable=False)

    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



    branch = db.Column(db.String(30), nullable=False)
    user_status = db.Column(db.String(20), nullable=False, default="Enabled")


class Ticket(db.Model):
    """ A table that contains all the ticket details """
    __tablename__ = "tickets"

    __table_args__ = {'extend_existing': True}

    ticket_id = db.Column(db.Integer, primary_key=True, autoincrement=False, unique=True)
    ticket_branch = ticket_type = db.Column(db.String(20), nullable=False)
    ticket_type = db.Column(db.String(20), nullable=False)
    ticket_category = db.Column(db.String(50), nullable=False)
    ticket_title = db.Column(db.String(100), nullable=True)
    ticket_details = db.Column(db.Text, nullable=True)

    #submission_date = db.Column(db.Date, nullable=False, default=func.now().cast(db.Date))
    # submission_date = db.Column(db.Date, nullable=True, default=func.now().cast(db.Date))

    submission_datetime = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc))

    #submission_time = db.Column(db.Time, nullable=False, default=text("TIME(CURRENT_TIMESTAMP)"))
    # submission_time = db.Column(db.Time, nullable=True, default=text("TIME(CURRENT_TIMESTAMP)"))

    # submission_time = db.Column(db.String(15), nullable=False)


    ticket_status = db.Column(db.String(20), nullable=False, default="Submitted")
    tickets = db.relationship("IT", backref=db.backref("ticket", lazy=True))


class IT(db.Model):
    """ A table that contains some ticket details for tech users only """
    __tablename__ = "it_tickets"

    __table_args__ = {'extend_existing': True}

    index = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.ticket_id'), nullable=False)
    tech_name = db.Column(db.String(30), nullable=True)
    update_date = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.now(timezone.utc))
    update_ticket_comment = db.Column(db.Text, nullable=True)

class UserTicket(db.Model):
    """ A linking table to link between the employee table and the ticket table """
    __tablename__ = "employee_ticket"

    __table_args__ = {'extend_existing': True}

    index = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.ticket_id'), nullable=False)
