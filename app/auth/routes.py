from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.models import db, User
from flask_login import login_user, logout_user, login_required
from app.auth.forms import RegisterForm, LoginForm
from flask_bcrypt import Bcrypt

auth = Blueprint("auth", __name__)
bcrypt = Bcrypt()

@auth.route("/registrar", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(name=form.name.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash("Usuário criado com sucesso!", "sucess")
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.first())
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Login realizado com sucesso.", "sucess")
            return redirect(url_for("home.index"))
        flash("Email ou senha incorretos.", "danger")
        return render_template("auth/login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logout realizado com sucesso.", "info")
    return redirect(url_for("auth.login"))