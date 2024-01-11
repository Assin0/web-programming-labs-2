from flask import Blueprint, render_template, request, redirect, session
import psycopg2

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/')
def main():
    return render_template('lab9/index.html')

@lab9.app_errorhandler(404)
def not_found(e):
    return render_template('lab9/error404.html')

@lab9.route('/lab9/500')
def error():
    result = 7 / 0
    return result

@lab9.app_errorhandler(500)
def error500(e):
    return render_template('lab9/error500.html')

@lab9.route('/lab9/otkritka', methods=['GET', 'POST'])
def otkritka():
    otkritka = ""
    username = request.form.get('username')
    username2 = request.form.get('username2')
    sex = request.form.get('sex')

    if username and username2 and sex == 'м':
        otkritka = f'Желаю счастья, чтобы  ты {username2} был самым здоровым человеком и в новом году ты получил все что желаешь! P. S. {username}'

    if username and username2 and sex == 'ж':
        otkritka = f'Желаю счастья, чтобы  ты {username2} была самым здоровым человеком и в новом году ты получила все что желаешь! P. S. {username}'
    return render_template('lab9/otkritka.html', otkritka=otkritka)