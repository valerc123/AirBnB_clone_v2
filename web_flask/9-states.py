#!/usr/bin/python3
"""
    Starts a Flask web application
"""
from flask import Flask, render_template
import models

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_sess(self):
    models.storage.close()


@app.route('/states_list')
def storage():
    obj = models.storage.all("State")
    return render_template('7-states_list.html', states=obj)


@app.route('/cities_by_states')
def cities_by_states():
    obj = models.storage.all('State')
    return render_template('8-cities_by_states.html', states=obj)


@app.route('/states')
@app.route('/states/<id>')
def states(id=None):
    obj = models.storage.all('State')
    return render_template('9-states.html', states=obj, id=id)


if __name__ == "__main__":
    app.run(debug=True)
