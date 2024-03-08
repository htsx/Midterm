from app import app
from flask import render_template, redirect, url_for
import sys

@app.route('/')
def main():
    return render_template('homepage.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/substract')
def substract():
    return render_template('substract.html')

@app.route('/multiply')
def multiply():
    return render_template('multiply.html')

@app.route('/divide')
def divide():
    return render_template('divide.html')

@app.route('/clear')
def clear():
    return render_template('clear.html')