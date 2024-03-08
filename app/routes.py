from app import app
from flask import render_template, redirect, url_for
import sys

@app.route('/')
def main():
    return render_template('homepage.html')

@app.route('/')
def add():
    return render_template('add.html')

@app.route('/')
def substract():
    return render_template('substract.html')

@app.route('/')
def multiply():
    return render_template('multiply.html')

@app.route('/')
def divide():
    return render_template('divide.html')

@app.route('/')
def clear():
    return render_template('clear.html')