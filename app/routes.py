from app import app
from flask import render_template, request

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/add', methods=['POST'])
def add():
    n1 = float(request.form['n1'])
    n2 = float(request.form['n2'])
    result = n1+n2
    return render_template('add.html', result=result)

@app.route('/sub', methods=['POST'])
def sub():
    n1 = float(request.form['n1'])
    n2 = float(request.form['n2'])
    result = n1+n2
    return render_template('substract.html', result=result)

@app.route('/mult', methods=['POST'])
def mult():
    n1 = float(request.form['n1'])
    n2 = float(request.form['n2'])
    result = n1+n2
    return render_template('multiply.html', result=result)

@app.route('/div', methods=['POST'])
def divide():
    n1 = float(request.form['n1'])
    n2 = float(request.form['n2'])
    result = n1+n2
    return render_template('divide.html', result=result)