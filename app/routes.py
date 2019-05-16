from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/prob1')
def prob1():
    return render_template('prob1.html')