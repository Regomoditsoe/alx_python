#!usr/bin/python3
#save this as app.py

from flask import Flask
from markupsafe import escape

@app.route ('/', stict_slashes=False)
def hello-hbnb():
    return "Hello HBNB!"

if __name__ '__main__':
    app.run(host='0.0.0.0', port=5000)
