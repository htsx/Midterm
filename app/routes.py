from app import app
from flask import render_template, redirect, url_for
import sys

@app.route('/')
def hello():
    return render_template('homepage.html')