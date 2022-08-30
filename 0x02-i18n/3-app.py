#!/usr/bin/env python3
"""Parametrize templates"""
from flask import Flask, request, render_template
from flask_babel import Babel


class Config(object):
    """Default configurations"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

    app = Flask(__name__)
    app.config.from_object(Config)
    babel = Babel(app)

    @app.route('/')
    def index():
        """Routes"""
        return render_template('3-index.html')

    if __name__ == '__main__':
        app.run(port='5000', host='0.0.0.0')
