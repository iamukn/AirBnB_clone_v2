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

if __name__ == "__main__":
    app.run(debug=True, port=5000)
