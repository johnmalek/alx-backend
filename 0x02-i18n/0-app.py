#!/usr/bin/env python3
"""
A python module
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """
    return home template
    """
    return render_template("index.html")
