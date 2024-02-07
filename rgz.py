from flask import Blueprint, render_template, request, redirect, session, jsonify
from Db import db
from Db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user
import psycopg2
from datetime import datetime

rgz = Blueprint('rgz', __name__)

@rgz.route("/rgz", methods=["GET", "POST"])
def login():
    errors = []
    if request.method == "GET":
        return render_template("login.html", errors=errors)

    username_form = request.form.get("username")
    password_form = request.form.get("password")

    if username_form == '' and password_form == '':
        errors.append("Поля не заполнены")
        return render_template("login.html", errors=errors)

    elif username_form == '':
        errors.append("Поле имени кладовщика не заполнено")
        return render_template("login.html", errors=errors)

    elif password_form == '':
        errors.append("Поле пароля кладовщика не заполнено")
        return render_template("login.html", errors=errors)

    my_user = users.query.filter_by(username=username_form).first()

    if my_user is not None:
        if check_password_hash(my_user.password, password_form):
            login_user(my_user, remember=False)
            return render_template("rgz/index.html")
        else:
            errors.append("Неправильный пароль")
            return render_template("login.html", errors=errors)
    else:
        errors.append("Такого кладовщика не существует")
        return render_template("login.html", errors=errors)
    
@rgz.route("/rgz/register", methods=["GET", "POST"])
def rgzregister():
    errors = []
    if request.method == "GET":
        return render_template("register.html", errors=errors)

    username_form = request.form.get("username")

    if username_form == '':
        errors.append("Не заполнены поля")
        return render_template("register.html", errors=errors)

    password_form = request.form.get("password")

    if len(password_form) < 5 or password_form == '':
        errors.append("Пароль меньше пяти символов")
        return render_template("register.html", errors=errors)

    isUserExist = users.query.filter_by(username=username_form).first()

    if isUserExist is not None:
        errors.append("Пользователь уже существует")
        return render_template("register.html", errors=errors)

    hashedPswd = generate_password_hash(password_form, method='pbkdf2')

    newUser = users(username=username_form, password=hashedPswd)

    db.session.add(newUser)

    db.session.commit()

    return redirect("/rgz")
    
tovari = [
    {"name": "пылесос", "count": 3, "article": 111},
    {"name": "пылесос", "count": 5, "article": 112},
    {"name": "пылесос", "count": 24, "article": 113},
    {"name": "пылесос", "count": 178, "article": 114},
    {"name": "пылесос", "count": 123, "article": 115},
    {"name": "пылесос", "count": 48, "article": 116},
    {"name": "пылесос", "count": 74, "article": 117},
    {"name": "пылесос", "count": 34, "article": 118},
    {"name": "пылесос", "count": 12, "article": 119},
    {"name": "пылесос", "count": 39, "article": 120},
    {"name": "холодильник", "count": 30, "article": 121},
    {"name": "холодильник", "count": 90, "article": 122},
    {"name": "холодильник", "count": 35, "article": 123},
    {"name": "холодильник", "count": 37, "article": 124},
    {"name": "холодильник", "count": 49, "article": 125},
    {"name": "холодильник", "count": 70, "article": 126},
    {"name": "холодильник", "count": 97, "article": 127},
    {"name": "холодильник", "count": 19, "article": 128},
    {"name": "холодильник", "count": 30, "article": 129},
    {"name": "холодильник", "count": 22, "article": 130},
    {"name": "фен", "count": 8, "article": 131},
    {"name": "фен", "count": 32, "article": 132},
    {"name": "фен", "count": 24, "article": 133},
    {"name": "фен", "count": 29, "article": 134},
    {"name": "фен", "count": 5, "article": 135},
    {"name": "фен", "count": 9, "article": 136},
    {"name": "фен", "count": 7, "article": 137},
    {"name": "фен", "count": 12, "article": 138},
    {"name": "фен", "count": 14, "article": 139},
    {"name": "фен", "count": 17, "article": 140},
]

@rgz.route('/rgz/api/tovari/', methods=['GET'])
def get_tovari():
    return jsonify(tovari)

@rgz.route('/rgz/api/tovari/<int:tovar_num>', methods=['GET'])
def get_tovar(tovar_num):
    if tovar_num in range(0, len(tovari)):
        return tovari[tovar_num]
    else:
        return "Нет такого товара", 404
    

@rgz.route('/rgz/api/tovari/<int:tovar_num>', methods=['DELETE'])
def del_tovar(tovar_num):
    if tovar_num in range(0, len(tovari)):
        del tovari[tovar_num]
        return '', 204
    else:
        return 'Нет такого товара', 404


@rgz.route('/rgz/api/tovari/<int:tovar_num>', methods=['PUT'])
def put_tovar(tovar_num):
    tovar = request.get_json()
    tovari[tovar_num] = tovar
    if tovar_num in range(0, len(tovari)):
        return tovari[tovar_num]
    else:
        return "Нет такого товара", 404
    

@rgz.route('/rgz/api/tovari/', methods=['POST'])
def add_tovar():
    tovar = request.get_json()
    tovari.append(tovar)
    return {'num': len(tovari) - 1}