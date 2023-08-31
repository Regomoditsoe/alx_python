#!/usr/bin/python3
"""Start a flask web application"""
# save this as app.py

from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route ('/', strict_slashes=False)
def hello():
    """Defining a route that returns the message HBNB"""
    return "HBNB"

def hello():
    """Defining a route that returns the message Hello HBNB!"""
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
