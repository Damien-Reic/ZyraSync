from ZyraSync.Models.Form.LoginForm import LoginForm
from ZyraSync.Models.Form.RegisterForm import RegisterForm
from ZyraSync.Models.Users.BasicUser import BasicUser
from ZyraSync.Models.Utilities.Logs import Logs
from ZyraSync import app
from ZyraSync import bcrypt
from ZyraSync import db
from flask_login import login_user, login_required, logout_user
from flask import render_template, redirect, url_for, request

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/admin", methods=["GET"])
@login_required
def admin():
    return render_template('admin.html')

@app.route("/login", methods=["GET","POST"])
@Logs.log_access
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = BasicUser.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                Logs.log_login()
                return redirect(url_for("admin"))
            else:
                Logs.log_login(username=f"<User '{form.username.data}'>", success=False)
    return render_template("login.html",form=form)


@app.route("/register", methods=["GET","POST"])
@Logs.log_access
def register():
    form = RegisterForm()
    wrong_password = request.args.get('wrong_password',default=False)
    if form.validate_on_submit():
        # Check if the password and password confirm are not the same
        if form.confirm_password.data != form.password.data:
            return redirect(url_for('register', wrong_password=True))
        BasicUser.register_user(form.username.data,form.password.data)
        return redirect(url_for('login'))
    return render_template("register.html", form=form, wrong_password=wrong_password)


@app.route("/logout",methods=["GET","POST"])
@Logs.log_access
def logout():
    Logs.log_logout()
    logout_user()
    return redirect(url_for("login"))


print("Views initialised")

