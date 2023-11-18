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
    
@lab4.route("/lab4/holo", methods = ['GET', 'POST'])
def holo():
    if request.method == 'GET':
        return render_template('holo.html')
    
    temp = request.form.get('temp')

    if temp == '':
        error = 'Не задана температура'
        return render_template('holo.html', error=error)
    elif int(temp) <= -12:
        error = 'Не удалось установить температуру - слишком низкое значение'
        return render_template('holo.html', error=error)
    elif int(temp) >= -1:
        error = 'Не удалось установить температуру - слишком высокое значение'
        return render_template('holo.html', error=error)
    elif -9 >= int(temp) > -12:
        error = 'Установлена температура '
        sneg = '***'
        return render_template('holo.html', temp=temp, error=error, sneg=sneg)
    elif -5 >= int(temp) >= -8:
        error = 'Установлена температура '
        sneg = '**'
        return render_template('holo.html', temp=temp, error=error, sneg=sneg)
    elif -1 > int(temp) >= -4:
        error = 'Установлена температура '
        sneg = '*'
        return render_template('holo.html', temp=temp, error=error, sneg=sneg)
