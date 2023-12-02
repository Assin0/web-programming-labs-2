from flask import Blueprint, render_template, request
import psycopg2

lab5 = Blueprint('lab5',__name__)

@lab5.route('/lab5')
def main():
    #Параметры подключения к бд
    conn = psycopg2.connect(
        host='127.0.0.1',
        database='knowledge_base_for_yura',
        user='yura_knowledge_base',
        password='123'
    )

    #Курсор для выполнения sql-запросов
    cur = conn.cursor()

    #Запрос для выполнения
    cur.execute("SELECT * FROM users;")

    # fetchall - получить все строки, которые получились в результате запроса
    # Сохраняем эти строки в переменную result
    result = cur.fetchall()

    # Закрываем соединение с БД
    cur.close()
    conn.close()

    print(result[0][0])

    return "go to console"