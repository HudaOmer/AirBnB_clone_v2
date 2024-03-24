#!/usr/bin/python3
"""This is my first flask project"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """This class returns a string with hello hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This class returns a string hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """This class returns c + some text"""
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is_cool'):
    """This class returns a string python + some text"""
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def n_is_number(n):
    """This class returns a string n is a number,int only"""
    return "{:d} is a number".format(n)

if __name__ == "__main__":
    """ The Main Function """
    app.run(host='0.0.0.0', port=5000)
