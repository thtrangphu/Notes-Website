from flask import Blueprint, render_template, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])

def login():
    data = request.form 
    print(data)
    return render_template('login.html', text = "Testing", user ="Note")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Please enter a valid email address', category='error')
        elif len(firstName) < 2:
            flash('Please enter a valid first name', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7: 
            flash('Password must be at least 7 characters', category='error')
        else:
            # add user to DB
            new_user = User(email = email, first_name = firstName, password = password1)
            flash('Account created!', category='success')

    return render_template('signup.html')