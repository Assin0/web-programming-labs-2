from flask import Blueprint, redirect, url_for, render_template, request
lab3 = Blueprint('lab3',__name__)


@lab3.route("/lab3/")
def lab():
    return render_template('lab3.html')


@lab3.route("/lab3/thanks")
def thanks():
    return render_template('thanks.html')


@lab3.route("/lab3/form1")
def form1():
    errors={}
    user=request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age=request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex=request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route("/lab3/order")
def order():
    return render_template('order.html')

@lab3.route("/lab3/pay")
def pay():
    price = 0
    drink=request.args.get('drink')
    # Пусть кофе стоит 120 рублей, черный чай 80 рублей, зеленый 70 рублей
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    # Добавка молока удорожает напиток на 30 рублей, а сахара на 10
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('pay.html', price=price)


@lab3.route("/lab3/ticket")
def ticket():
    errors={}
    name=request.args.get('name')
    if name == '':
        errors['name'] = 'Заполните поле!'
    type=request.args.get('type')
    if type == '':
        errors['type'] = 'Заполните поле!'
    polka=request.args.get('polka')
    if polka == '':
        errors['polka'] = 'Заполните поле!'
    bagag=request.args.get('bagag')
    if bagag == '':
        errors['bagag'] = 'Заполните поле!'
    ages=request.args.get('ages')
    if ages == '':
        errors['ages'] = 'Заполните поле!'
    otkuda=request.args.get('otkuda')
    if otkuda == '':
        errors['otkuda'] = 'Заполните поле!'
    kuda=request.args.get('kuda')
    if kuda == '':
        errors['kuda'] = 'Заполните поле!'
    date=request.args.get('date')
    if date == '':
        errors['date'] = 'Заполните поле!'
    
    
    return render_template('ticket.html', name=name, errors=errors, type=type, polka=polka, bagag=bagag, ages=ages, otkuda=otkuda, kuda=kuda, date=date)


@lab3.route("/lab3/blag")
def blag():
    return render_template('blag.html')