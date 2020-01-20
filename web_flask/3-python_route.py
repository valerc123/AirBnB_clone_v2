#!/usr/bin/python3
"""
    Starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def app_1():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def app_2(text):
    return "C {}".format(text.replace('_', ' '))

@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False, defaults={'text': 'is cool'})
def app_3(text):
    return "Python {}".format(text.replace('_', ' '))

app.run()
