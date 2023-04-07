#!/usr/bin/python3
"""First flask module for HBNB"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from os import getenv

app = Flask(__name__)
env = getenv('HBNB_TYPE_STORAGE')


@app.teardown_appcontext
def teardown_close(self):
    "Closses SQLAlchemy session"
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Returns a HTML file with states list"""
    states_list = storage.all(State).values()
    amenities_list = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', st_list=states_list, amnt_list=amenities_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
