from app import app
from flask import render_template, redirect, request

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/add')
def home():
    return render_template('add.html')