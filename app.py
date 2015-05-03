__author__ = 'Isaac'
from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def do():
    f = open('index.html', 'r')
    return f.read()

@app.route('/sss')
def dos():
    f = open('sss.html', 'r')
    return f.read()
