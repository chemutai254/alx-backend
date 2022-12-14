#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask, render_template
from flask_babel import Babel
# app = Flask(__name__)


class Config(object):
    """Use class config for the app"""
    LANGUAGES = ['en', 'fr']
    """sets local to english and timezone to UTC"""
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

    app = Flask(__name__)
    app.config.from_object(Config)
    babel = Babel(app)

    @app.route('/')
    def index():
        """Use routes"""
        return render_template("1-index.html")

    if __name__ == '__main__':
        app.run(port='5000', host='0.0.0.0')
