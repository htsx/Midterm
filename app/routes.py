from app import app
from flask import render_template, redirect, url_for
import sys

@app.route('/')
def main():
    return render_template('homepage.html')

@app.route('/add')
def add():
    num1 = request.form['num1']
    num2 = request.form['num2']
    add = request.form['add']
    result = float(num1) + float(num2)
    return render_template('add.html', result=result)
