__author__ = 'Isaac'
from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def do():
    return render_template('index.html')

@app.route('/sss')
def dos():
    return render_template('sss.html')
