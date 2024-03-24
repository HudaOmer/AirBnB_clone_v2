#!/usr/bin/python3
"""This is my first flask project"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """This class returns a string with hello hbnb'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """This class returns a string with hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """This class returns a string with c + some text"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """This class returns a string Python + some text"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """This class returns a string n is a number, n int only"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """displays an HTML page only if <n> is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """displays an HTML page and shows if <n> is even/odd"""
    return render_template("6-number_odd_or_even.py", n=n)


if __name__ == "__main__":
    """ The Main Function """
    app.run(host='0.0.0.0', port=5000)
