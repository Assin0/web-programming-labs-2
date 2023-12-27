from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, redirect, session
import psycopg2

lab5 = Blueprint('lab5',__name__)

def dbConnect():
    #Параметры подключения к бд
    conn = psycopg2.connect(
        host='127.0.0.1',
        database='knowledge_base_for_yura',
        user='yura_knowledge_base',
        password='123'
    )

    return conn;

def dbClose(cursor, connection):
    #Закрываем  курсор и соединение
    cursor.close()
    connection.close()

@lab5.route('/lab5/first')
def nain():
    conn = dbConnect()
    cur = conn.cursor() #Курсор для выполнения sql-запросов

    cur.execute("SELECT * FROM users;") #Запрос для выполнения

    # fetchall - получить все строки, которые получились в результате запроса
    # Сохраняем эти строки в переменную result
    result = cur.fetchall()

    print(result[0][0])

    # Закрываем соединение с БД
    dbClose(cur, conn)

    return "go to console"

@lab5.route('/lab5')
def main():
    if session['username'] is None:
        visibleUser = "Anon"
    else:
        visibleUser = session['username']

    return render_template("lab5.html", username=visibleUser)

@lab5.route('/lab5/register', methods=['GET', 'POST'])
def registerPage():
    errors = ""

    if request.method == 'GET':
        return render_template('register.html', errors=errors)
    
    username = request.form.get('username')
    password = request.form.get('password')

    if not (username or password):
        errors = 'Пожалуйста, заполните все поля'
        return render_template('register.html', errors=errors)
    
    hashPassword = generate_password_hash(password)
    
    conn = dbConnect ()
    cur = conn.cursor ()

    cur.execute(f"SELECT username FROM users WHERE username = '{username}';")

    if cur.fetchone() is not None:
        errors = "Пользователь с таким именем уже существует"
        
        dbClose(cur, conn)
        return render_template("register.html", errors=errors)
    
    cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}','{hashPassword}');")

    conn.commit()
    dbClose(cur, conn)

    return redirect("/lab5/log")

@lab5.route("/lab5/log", methods=["GET", "POST"])
def log():
    errors = ""

    if request.method == "GET":
        return render_template('log.html', errors=errors)
    
    username = request.form.get("username")
    password = request.form.get("password")

    if not (username or password):
        errors = "Пожалуйста заполните все поля"
        return render_template("log.html", errors=errors)
    
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(f"SELECT id, password FROM users WHERE username = '{username}'")

    result = cur.fetchone()

    if result is None:
        errors = "Неправильный логин или пароль"
        dbClose(cur, conn)
        return render_template("log.html", errors=errors)
    
    userID, hashPassword = result

    if check_password_hash(hashPassword, password):

        session['id'] = userID
        session['username'] = username
        dbClose(cur,conn)
        return redirect("/lab5")
    
    else:
        errors = "Неправильный логин или пароль"
        return render_template("log.html", errors=errors)
    
@lab5.route("/lab5/zametki", methods=["GET", "POST"])
def zam():
    errors = ""

    userID = session.get("id")

if userID is not None:
    if request.method == "GET":
        return render_template('zametki.html')
    
    if request.method == "POST":
        text_article = request.form.get("text_article")
        title = request.form.get('title_article')

        if len(text_article) == 0:
            errors = "Заполните текст"
            return render_template('zametki.html', errors=errors)
        
        conn= dbConnect()
        cur = conn.cursor()

        cur.execute(f"INSERT INTO articles(user_id, title, article_text) VALUES ({userID}, '{title}','{text_article}') RETURNING id")

        new_article_id = cur.fetchone()[0]
        conn.commit()

        dbClose(cur,conn)

        return redirect (f'/lab5/zametki/{new_article_id}')
    
return redirect('/lab5/login')