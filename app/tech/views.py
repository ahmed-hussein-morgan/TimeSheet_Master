# type: ignore
from flask import render_template, redirect, request, url_for, flash, current_app
from . import tech
#from flask_login import login_user, logout_user, login_required, current_user
from ..models import UserLogin, Employee, Attendance
from .forms import NewUserForm, NewEmployeeForm, SearchAttendanceDate
from .. import db
from datetime import datetime, timezone
from sqlalchemy import or_, update
from zk import ZK
import xlsxwriter



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
    conn = None
    zk = ZK('192.168.1.203', port=4370, timeout=50)

    try:
        conn = zk.connect()
        flash(f'Successful connection to ZK machine ip: 192.168.1.203\n Error is: {error_message}.', 'success')

        attendances = conn.get_attendance()

        if form.validate_on_submit:
            starting_date = start_date.data
            ending_date = end_date.data
            for attendance in attendances:
                parts = attendance_str.split(': ')
                attendance_id = str(parts[1])
                timestamp_str = parts[2].split(' ')[0] + ' ' + parts[2].split(' ')[1]
                status_tuple = eval(parts[2].split('(')[1].strip(')'))

                attendance_data = {
                    'attendance_id': attendance_id,
                    'timestamp': timestamp_str,
                    'status': status_tuple
                }

        return render_template("attendance_raw.html", title="TimeSheet - Attendance", form=form)
    except Exception as e:
        error_message = str(e)
        return flash(f'Failed to connect to ZK machine ip: 192.168.1.203\n Error is: {error_message}.', 'danger')
    finally:
        if conn:
            conn.disconnect()

            user = User(employee_id = user_id, employee_name=user_name, department=user_department, job_title=user_job, role_type=user_type, email=email, branch=user_branch, user_status=user_status)
            user.set_password(password)
            
            
            db.session.add(user)
            db.session.commit()
            
            flash(f'User created successfully for {form.user_name.data}.', 'success')

@tech.route("/calculated")
def tech_calculated_data():
    form = SearchAttendanceDate()
    return render_template("attendance_calculated.html", title="TimeSheet - Attendance", form=form)

@tech.route("/export")
def export_to_excel():
    pass
    # form = SearchAttendanceDate()

    # return render_template("attendance_calculated.html", title="TimeSheet - Attendance", form=form)
