#!/usr/bin/python3
"""
    Starts a Flask web application
"""
from flask import Flask, render_template
import models

app = Flask(__name__)


@app.teardown_appcontext
def close_sess(self):
    models.storage.close()


@app.route('/states_list', strict_slashes=False)
def storage():
    store = models.storage.all("State")
    return render_template('7-states_list.html', states=store)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    obj = models.storage.all('State')
    return render_template('8-cities_by_states.html', states=obj)

if __name__ == "__main__":
    app.run(debug=True)
