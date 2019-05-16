from flask import render_template, request
from app import app
from problem1 import Problem1

import csv
import math



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/prob1', methods=['GET', 'POST'])
def prob1():
    if request.method=='POST':
        starID = request.form['starID']
        starlist = Problem1(starID)
        return render_template('prob1result.html', results=starlist, starID=starID)
    return render_template('prob1.html')
    