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


@app.route('/hbnb_filters')
def filters():
    models.storage.all('')

if __name__ == "__main__":
    app.run(debug=True)
