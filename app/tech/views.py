# type: ignore
from flask import render_template, redirect, request, url_for, flash, current_app
from . import tech
#from flask_login import login_user, logout_user, login_required, current_user
from ..models import UserLogin, Employee
from .forms import NewUserForm, NewEmployeeForm, SearchAttendanceDate
from .. import db
from datetime import datetime, timezone
from sqlalchemy import or_, update



@tech.route("/new-user", methods=["GET", "POST"])
def tech_new_user():
    form = NewUserForm()
    return render_template("tech_add_user.html", title="TimeSheet - New User", form=form)



@tech.route("/all-users")
def tech_all_users():
    users = UserLogin.query.all()
    return render_template("tech_all_users.html", title="TimeSheet - All Users", users=users)
    # return render_template("tech_all_users.html", title="TimeSheet - All Users")


@tech.route("/new-employee", methods=["GET", "POST"])
def tech_new_employee():
    form = NewEmployeeForm()
    return render_template("tech_add_employee.html", title="TimeSheet - New Employee", form=form)


@tech.route("/all-employees")
def tech_all_employees():
    employees = Employee.query.all()
    return render_template("tech_all_employees.html", title="TimeSheet - All Employees", employees=employees)


# @tech.route("/machines")
# def tech_all_machines():
#     machines = Machine.query.all()
#     return render_template("tech_machines.html", title="TimeSheet - Machines", machines=machines)

@tech.route("/attendance")
def tech_raw_data():
    form = SearchAttendanceDate()

    return render_template("attendance_raw.html", title="TimeSheet - Attendance", form=form)

@tech.route("/calculated")
def tech_calculated_data():
    form = SearchAttendanceDate()

    return render_template("attendance_calculated.html", title="TimeSheet - Attendance", form=form)
