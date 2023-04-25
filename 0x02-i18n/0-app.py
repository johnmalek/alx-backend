#!/usr/bin/env python3
"""
A python flask app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """
    handle / route
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(port="8000", host="0.0.0.0", debug=True)
