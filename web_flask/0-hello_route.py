#!/usr/bin/python3
"""This is my first flask project"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/airbnb-onepage/")
def hello_hbnb():
    """This class returns a string with helllo hbnb"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
