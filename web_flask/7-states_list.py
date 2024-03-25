#!/usr/bin/python3
"""Display a HTML page: (inside the tag BODY)"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(exc):
    """This class closes the current session of sqlalchemist"""
    storage.close()


@app.route('/states_list')
def states_list():
    """This class displays a HTML page: (inside the tag BODY)"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    """The Main Function"""
    app.run(host='0.0.0.0', port=5000, debug=True)
