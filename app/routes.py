from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User
from app.forms import LoginForm, RegistrationForm
from app import db

bp = Blueprint('routes', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('routes.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        print("Registration successful!")
        return redirect(url_for('routes.login'))
    return render_template('register.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    #if current_user.is_authenticated:  # Redirect if already logged in
        #print("His")
        #return redirect(url_for('routes.index'))

    print("Login page reached")
    form = LoginForm()

    if form.validate_on_submit():  # If form is valid
        print(f"Attempting to log in user: {form.username.data}")

        user = User.query.filter_by(username=form.username.data).first()  # Find user by username
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('routes.index'))
        else:
            flash('Invalid email or password.', 'danger')

    return render_template('login.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    print("Logged out.")
    return redirect(url_for('routes.index'))

@bp.route('/')
@login_required
def index():
    return render_template('index.html')

@bp.route('/debate/<topic_id>')
def debate(topic_id):
    if topic_id == '1':
        return render_template('debate1.html', topic_id=topic_id)
    elif topic_id == '2':
        return render_template('debate2.html', topic_id=topic_id)
    elif topic_id == '3':
        return render_template('debate3.html', topic_id=topic_id)
    else:
        return render_template('error.html', message="Topic not found"), 404

@bp.route('/test', methods=['GET'])
def test():
    print("Test route accessed")
    return "Test successful"
