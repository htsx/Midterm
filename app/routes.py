from app import app
from flask import Flask, render_template, redirect, request

@app.route('/')
def hello():
    return render_template('homepage.html')
