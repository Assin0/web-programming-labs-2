from flask import Blueprint, render_template, request, redirect, session
from Db import db
from Db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user
import psycopg2

lab6 = Blueprint('lab6', __name__)

@lab6.route('/lab6/')
def main():
    return render_template('lab6.html')

@lab6.route("/lab6/check")
def check():
    my_users = users.query.all()
    print(my_users)
    return "result in console"

@lab6.route("/lab6/checkarticles")
def checkarticles():
    my_articles = articles.query.all()
    print(my_articles)
    return "result in console"

@lab6.route("/lab6/register", methods=["GET", "POST"])
def register():
    errors = []
    if request.method == "GET":
        return render_template("register6.html", errors=errors)

    username_form = request.form.get("username")

    if username_form == '':
        errors.append("Пустое имя")
        return render_template("register6.html", errors=errors)

    password_form = request.form.get("password")

    if len(password_form) < 5 or password_form == '':
        errors.append("Пароль меньше пяти символов")
        return render_template("register6.html", errors=errors)

    isUserExist = users.query.filter_by(username=username_form).first()

    if isUserExist is not None:
        errors.append("Пользователь уже существует")
        return render_template("register6.html", errors=errors)  # Вывод ошибки

    hashedPswd = generate_password_hash(password_form, method='pbkdf2')

    newUser = users(username=username_form, password=hashedPswd)

    db.session.add(newUser)

    db.session.commit()

    return redirect("/lab6/login")

@lab6.route("/lab6/login", methods=["GET", "POST"])
def login():
    errors = []
    if request.method == "GET":
        return render_template("login6.html", errors=errors)

    username_form = request.form.get("username")
    password_form = request.form.get("password")

    if username_form == '' and password_form == '':
        errors.append("Поля не заполнены")
        return render_template("login6.html", errors=errors)

    elif username_form == '':
        errors.append("Поле username_form не заполнено")
        return render_template("login6.html", errors=errors)

    elif password_form == '':
        errors.append("Поле password_form не заполнено")
        return render_template("login6.html", errors=errors)

    my_user = users.query.filter_by(username=username_form).first()

    if my_user is not None:
        if check_password_hash(my_user.password, password_form):
            login_user(my_user, remember=False)
            return redirect("/lab6/articles")
        else:
            errors.append("Неправильный пароль")
            return render_template("login6.html", errors=errors)
    else:
        errors.append("Пользователя не существует")
        return render_template("login6.html", errors=errors)
    
@lab6.route("/lab6/articles/")
@login_required
def articles_list():
    my_articles = articles.query.filter_by(user_id=current_user.id).all()
    return render_template("AllArtShow.html", articles=my_articles)


@lab6.route("/lab6/logout")
@login_required
def logout():
    logout_user()
    return redirect("/lab6/")