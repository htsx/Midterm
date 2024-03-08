from app import app
from flask import render_template, request

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    n1 = float(request.form['n1'])
    n2 = float(request.form['n2'])
    result = n1+n2
    return render_template('add.html', result=result)

@app.route('/add', methods=['GET', 'POST'])
def sub():
    return render_template('add.html')

@app.route('/add', methods=['GET', 'POST'])
def mult():
    return render_template('add.html')

@app.route('/add', methods=['GET', 'POST'])
def div():
    return render_template('add.html')