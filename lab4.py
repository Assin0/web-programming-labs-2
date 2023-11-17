from flask import Blueprint, render_template, request
lab4 = Blueprint('lab4',__name__)


@lab4.route("/lab4/")
def lab():
    return render_template('lab4.html')

@lab4.route("/lab4/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'alex' and password == '123':
        return render_template('success.html', username=username)
    elif username == '' or password == '':
        error = 'Не введён логин или не введён пароль'
        username = username
        password = password
        return render_template('login.html', error=error, username=username, password=password)
    else:
        error = 'Неверный логин и/или пароль'
        username = username
        password = password
        return render_template('login.html', error=error, username=username, password=password)
    
