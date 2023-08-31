#!/usr/bin/python3
"""Start a flask web application"""
# save this as app.py

from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route ('/', strict_slashes=False)
def hello():
    """Defining a route that returns the message Hello HBNB!"""
    name = request.args.get("name", "HBNB")
    return f"Hello {escape(name)}!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Defining the route returning the message HBNB"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Defining a C route followed by value of text"""
    text = text.replace("_", " ")
    return f"C {escape(text)}"

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """Defining a Python text followed by value of text"""
    text = text.replace("_", " ")
    return f"Python {escape(text)}"

@app.route('/number/<int:n>', strict_slashes=False)
def a_number(n):
    """Defining a route if n is an integer"""
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Defining a number template on HTML page wher n is integer"""
    return render_template('5-number.html', number=n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
