from flask import Blueprint, render_template

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