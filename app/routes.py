from flask import render_template, request
from app import app
from problem1 import Problem1
from problem3 import Problem3
from problem2 import Problem2
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
    
@app.route('/prob3')
def prob3():
    results = Problem3()
    return render_template('prob3.html', results=results)

@app.route('/prob2')
def prob2():
    results = Problem2()
    return render_template('prob2.html', results=results)
