#!/usr/bin/env python3
"""
A python flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


def get_user():
    """
    Returns a user dictionary or None if the ID
    cannot be found or if login_as was not passed
    """
    user_id = request.args.get('login_as', None)
    if user_id and int(user_id) in users.keys():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """
    Add user to flask.g if user is found
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """
    Determine the best match with supported languages
    """
    lang = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang
    if g.user:
        lang = g.user.get('locale')
        if lang and lang in app.config['LANGUAGES']:
            return lang
    lang = request.headers.get('locale', None)
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_language.best_match(app.config['LANGUAGES'])


@app.route("/")
def home() -> str:
    """
    handle / route
    """
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(port="8000", host="0.0.0.0", debug=True)
