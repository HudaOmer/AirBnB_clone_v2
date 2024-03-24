#!/usr/bin/python3
"""This is my first flask project"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """This class returns a string with hello hbnb"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """This class returns a string hbnb"""
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    """This class returns a string c + some text"""
    return "C " + text.replace('_', ' ')


@app.route("/python")
@app.route("/python/<text>")
def python_is_cool(text="is cool"):
    """This class returns a string python + some text"""
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>')
def n_is_a_number(n):
    """This class returns a string int n + is number"""
    return "{} is a number".formt(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
