#!/usr/bin/env python3
"""
A python flask app
"""
from flask import Flask, render_template, request
from babel import Babel


class Config(object):
    """
    Configure babel for app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determine the best match with supported languages
    """
    lang = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_language.best_match(app.config['LANGUAGES'])


@app.route("/")
def home() -> str:
    """
    handle / route
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(port="8000", host="0.0.0.0", debug=True)