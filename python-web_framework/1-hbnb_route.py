#!/usr/bin/python3
"""Start a flask web application"""
# save this as app.py

from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route ('/', strict_slashes=False)
def combined_route():
    """Defining a route that returns the message HBNB and Hello HBNB!"""
    return "HBNB\nHello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
