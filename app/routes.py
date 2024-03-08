from app import app
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/add', methods=['POST'])
def add():
    n1 = float(request.form['n1'])
    n2 = float(request.form['n2'])
    result = n1+n2
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)