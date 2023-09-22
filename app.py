from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <ol>
        <li><a href="http://127.0.0.1:5000/lab1" target="_blank">Первая лабораторная</a></li>
        </ol>

        <footer>
            &copy; ФИО, группа, курс, год
        </footer>
    </body>
</html>
"""

@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <title>Комаров Юрий Павлович, лабораторная №1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>

        <footer>
            &copy; Юрий Комаров, ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
"""

@app.route("/lab1/oak")
def oak():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
'''