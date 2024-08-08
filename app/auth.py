from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('passwd')
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("logout.html")

#form validations
@auth.route('/sign-up', methods=['GET' ,'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('name')
        password = request.form.get('passwd')
        confirm_password = request.form.get('passwd2')

        #Validity of forms
        if len(email) < 4:
            flash("Email must be greater than 4 characters.", category='error')
        elif len(first_name) < 2:
            flash("First name must be greater than 2 characters", category='error')
        elif password != confirm_password:
            flash("The Password's must match", category='error')
        elif len(password) < 7:
            flash("Password must be atleast 7 charaters long.", category='error')
        else:
            flash("Account created successfully", category='success')

    return render_template("signup.html")
