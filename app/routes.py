from app import app
from flask import Flask, render_template, redirect, url_for, request
import sys

@app.route('/')
def main():
    return render_template('homepage.html')

@app.route('/', methods=['GET',"POST"])
def add():
    if request.method == "POST":
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        add = float(num1) + float(num2)
        result = float(num1) + float(num2)
        return render_template('add.html', add=add)
    return render_template('homepage.html')
