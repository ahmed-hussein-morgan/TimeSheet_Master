# type: ignore
from flask import render_template, redirect, request, url_for, flash, current_app
from . import tech
#from flask_login import login_user, logout_user, login_required, current_user
from ..models import UserLogin, Employee, Attendance, Machine
from .forms import NewUserForm, SearchTicketForm, SearchUserForm, NewTicketForm, UpdateUserForm
from .. import db
from datetime import datetime, timezone
from sqlalchemy import or_, update

@tech.route("/new-user", methods=["GET", "POST"])
def tech_new_user():
    return render_template("tech_add_user.html", title="TimeSheet - New User")



@tech.route("/all-users", methods=["GET", "POST"])
def tech_all_users():
    users = UserLogin.query.all()
    return render_template("tech_all_users.html", title="TimeSheet - All Users", users=users)


@tech.route("/new-employee", methods=["GET", "POST"])
def tech_new_employee():
    return render_template("tech_add_employee.html", title="TimeSheet - New Employee")


@tech.route("/all-employees", methods=["GET", "POST"])
def tech_all_employees():
    return render_template("tech_all_employees.html", title="TimeSheet - All Employees")
