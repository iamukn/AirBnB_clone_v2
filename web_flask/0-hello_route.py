#!/usr/bin/python3
""" Importing flask, creating an instance and
working with it"""

from flask import Flask

app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def home():
    """This prints Hello HBNB! when the root is accessed
    """
    return ('Hello HBNB!')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
