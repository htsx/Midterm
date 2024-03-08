from app import app
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/', methods=['GET',"POST"])
def add():
    if request.method == "POST":
        n1 = request.form.get('n1')
        n2 = request.form.get('n2')
        add = float(n1) + float(n2)
    return render_template('add.html')
