from app import app
from flask import render_template, redirect, url_for
import sys

@app.route('/')
def main():
    return render_template('homepage.html')

@app.route('/add', methods=['GET',"POST"])
def add():
    if request.method == "POST":
        num1 = request.form['num1']
        num2 = request.form['num2']
        add = float(num1) + float(num2)
        result = float(num1) + float(num2)
        return render_template('add.html', add=add)
    return render_template('homepage.html')
