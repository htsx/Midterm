from app import app
from flask import Flask, render_template, redirect, request

@app.route('/', methods=['GET',"POST"])
def add():
    if request.method == "POST":
        n1 = request.form.get('num1')
        n2 = request.form.get('num2')
        add = float(num1) + float(num2)
        return render_template('add.html', add=add)
    return render_template('homepage.html')
