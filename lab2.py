from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2',__name__)


@lab2.route('/')
@lab2.route("/index")
def start():
    return redirect("/menu", code=302)


@lab2.route("/lab2/buket")
def buket():
    return render_template('buket.html')


@lab2.route("/lab2/")
def lab():
    return render_template('lab2.html')


@lab2.route("/lab2/example")
def example():
    name= "Юрий Комаров"
    number="2"
    group="ФБИ-11"
    course="3 курс"
    fruits = [
        {'name':'яблоки', 'price': 100},
        {'name':'груши', 'price': 120},
        {'name':'апельсины', 'price': 80},
        {'name':'мандарины', 'price': 95},
        {'name':'манго', 'price': 321}
        ]
    books = [
        {'author':'Джоан Роулинг', 'name': 'Гарри Поттер и узник Азкабана', 'genre': 'Фантастика',  'pages': 544},
        {'author':'Стивен Кинг', 'name': 'Зеленая миля', 'genre': 'Ужасы',  'pages': 384},
        {'author':'Маргарет Митчелл', 'name': 'Унесенные ветром', 'genre': 'Роман',  'pages': 1088},
        {'author':'Артур Конан Дойл', 'name': 'Шерлок Холмс', 'genre': 'Детектив',  'pages': 944},
        {'author':'Нора Сакавич', 'name': 'Свита короля', 'genre': 'Роман',  'pages': 120},
        {'author':'Мишель Пейвер', 'name': 'Гарри Поттер и Принц-полукровка', 'genre': 'Фантастика',  'pages': 976},
        {'author':'Мосян Тунсю', 'name': 'Благословение небожителей. Том 1', 'genre': 'Фэнтези',  'pages': 416},
        {'author':'Мосян Тунсю', 'name': 'Благословение небожителей. Том 3', 'genre': 'Фэнтези',  'pages': 384},
        {'author':'Кэтрин Стокетт', 'name': 'Прислуга', 'genre': 'Роман',  'pages': 576},
        {'author':'Александр Дюма', 'name': 'Граф Монте-Кристо', 'genre': 'Роман',  'pages': 1264}
        ]
    return render_template("example.html", name=name, number=number, group=group, course=course, fruits=fruits, books=books)