# type: ignore
from flask import render_template, redirect, request, url_for, flash
from . import auth
from .. import tech, non_tech
#from flask_login import login_user, logout_user, login_required, current_user
from ..models import UserLogin
from .forms import LoginForm

@auth.route('/', methods=['GET', 'POST'])
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = UserLogin.query.filter_by(employee_name=form.user_name.data).first()
        if user and user.check_password(form.password.data):
        # if user and user.check_password(password_hash, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            current_user_type = User.query.filter_by(role_type=user.role_type).first()
            current_user_name = User.query.filter_by(employee_name=user.employee_name).first()

            if current_user_type == "tech":
                flash(f"Welcome {current_user_name}.", 'success')
                if next_page and next_page.startswith('/'):
                    return redirect(next_page)
                return redirect(url_for('tech.tech_dashboard'))
            
            elif current_user_type == "non-tech":
                flash(f"Welcome {current_user_name}.", 'success')
                if next_page and next_page.startswith('/'):
                    return redirect(next_page)
                return redirect(url_for('non_tech.all_ticket'))
        else:
            flash(f"Login Failed. Please check User ID and password", "dangerous")

    return render_template('login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))
