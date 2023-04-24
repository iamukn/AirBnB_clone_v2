#!/usr/bin/python3
""" Importing flask, creating an instance and
working with it to serve / and /HBNB page"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """This prints Hello HBNB! when the root is accessed
    """
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Serves the content of HBNB
    """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    split = text.replace('_', ' ')
    return ("C {0}".format(split))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def double_route(text="is cool"):
    """serves the /python page and /python/<text>
    """
    if text:
        replace = text.replace('_', ' ')
        return ("Python {0}".format(replace))
    else:
        return ("Python {0}".format(text))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
