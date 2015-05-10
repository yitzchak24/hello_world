from flask import render_template, request
from app import app

@app.rout('/')
def index():
  return render_template('index.html')
