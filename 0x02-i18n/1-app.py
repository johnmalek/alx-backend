#!/usr/bin/env python3
"""
A python flask app
"""
from flask import Flask, render_template
from babel_babel import Babel
import pytz

app = Flask(__name__)
babel = Babel(app)


class Config(babel):
    """
    Configure babel for app
    """
    LANGUAGES = ["en", "fr"]
    default_locale = "en"
    default_timezone = "UTC"


@app.route("/")
def home():
    """
    handle / route
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(port="home", host="0.0.0.0", debug=True)
