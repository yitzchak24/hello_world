__author__ = 'Isaac'
from flask import Flask
from flask import render_template, request

app = Flask(__name__)

def loadPage(url):
    f = open(url, 'r')
    return f.read()

@app.route('/')
def do():
    loadPage('index.txt')

@app.route('/sss')
def dos():
    loadPage('sss.html')