#!/usr/bin/python3
"""
    Starts a Flask web application
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False, defaults={'text': 'is cool'})
def py_route(text):
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def num_route(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    if n % 2 == 0:
        odd_even = 'even'
    else:
        odd_even = 'odd'
    return render_template('6-number_odd_or_even.html',
                           odd_or_even=odd_even, num=n)

if __name__ == "__main__":
    app.run(debug=True)
