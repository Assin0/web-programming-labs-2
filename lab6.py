from flask import Blueprint, render_template, request, redirect, session
import psycopg2

lab6 = Blueprint('lab6', __name__)

@lab6.route('/lab6/')
def main():
    return render_template('lab6.html')